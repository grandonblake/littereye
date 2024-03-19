from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy, QAbstractSpinBox, QDateEdit,
    QStatusBar, QVBoxLayout, QWidget, QDialog, QLayout, QSlider, QDialogButtonBox, QTabWidget)

from PySide6 import QtWidgets
from PySide6.QtCore import Signal, QThread
from ultralytics import YOLO
import os, sys, datetime, time, cv2

from ui import Ui_MainWindow, Ui_Dialog, settingsDialogBox

from database import Database

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class VideoWorker(QObject):
    imageUpdated = Signal(QImage)
    errorOccurred = Signal(str)
    objectListUpdated = Signal(list)
    def __init__(self, capture, model_index, conf, iou, models, maxID, is_recording=False):
        super().__init__()
        self.capture = capture
        self.model_index = model_index
        self.conf = conf
        self.iou = iou
        self.models = [YOLO(model) for model in models]
        self.is_recording = is_recording # Flag to track recording state
        self.recording_out = None  # Video writer object
        self.maxID = maxID
        self.fps = 0.0

    def run(self):
        global start_time, frames

        frames = 0  # Initialize frame count
        start_time = time.time()  # Initialize start time 

        while True:
            ret, frame = self.capture.read()
            if ret:
                # Run YOLOv8 inference on the frame
                results = self.models[self.model_index].track(frame, stream=True, persist=True, conf=self.conf, iou=self.iou)
                detected_objects = {}

                for result in results:
                    # Visualize the results on the frame
                    frame = result.plot()
                    names = result.names 
                    classes = result.boxes.cls 
                    ids = result.boxes.id
                    conf = result.boxes.conf

                    # Check if ids and classes are not None
                    if ids is not None and classes is not None:
                        # Convert the tensors to lists
                        ids_list = ids.tolist()
                        classes_list = classes.tolist()
                        conf_list = conf.tolist()

                        # Iterate over both lists simultaneously
                        for i in range(len(ids_list)):
                            object_id = int(ids_list[i])  # Convert the ID to an integer
                            class_index = int(classes_list[i])  # Convert the class index to an integer
                            object_conf = conf_list[i]  # Get the confidence score as is
                            object_name = names[class_index]  # Get the corresponding name for the class index
                            detected_objects[object_id] = (object_name, object_conf)  # Assign the name and conf to the ID in the dictionary

                            datetimeNow = datetime.datetime.now()  # Get the current time
                            formattedDateTimeNow = datetimeNow.strftime("%m-%d-%Y %H-%M-%S")  # date and time in 24H format
                            
                            # {0: 'Cardboard', 1: 'Drink carton', 2: 'Face mask', 3: 'Glass bottle', 4: 'Metal can', 
                            # 5: 'Paper bag', 6: 'Paper container', 7: 'Paper cup', 8: 'Plastic bag', 9: 'Plastic bottle', 
                            # 10: 'Plastic cup', 11: 'Plastic wrapper', 12: 'Rags', 13: 'Styrofoam'}

                            if(class_index == 2 or class_index == 12 or class_index == 13): #not recyclable
                                recyclableBool = 0
                            else: #recyclable
                                recyclableBool = 1

                            maxID = self.maxID + object_id

                            with Database() as database:
                                database.insertObject(objectID=maxID, className=object_name, confidenceLevel=object_conf, recyclableBool=recyclableBool, dateTime=formattedDateTimeNow)

                                database.selectAll()

                # Emit the detected objects list, even if it's empty
                self.objectListUpdated.emit(list(detected_objects.values()))

                # Calculate FPS
                fps = self.calculate_fps() 

                # Draw FPS text on the frame
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 0.5
                font_thickness = 1
                text_color = (0, 0, 255)
                text_size, _ = cv2.getTextSize("FPS: {:.2f}".format(fps), font, font_scale, font_thickness)
                text_origin = (frame.shape[1] - text_size[0] - 10, 30) 

                cv2.putText(frame, "FPS: {:.2f}".format(fps), text_origin, font, font_scale, text_color, font_thickness)

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                self.imageUpdated.emit(image.copy())

                if self.is_recording:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    font_scale = 0.5  # Adjust font size as needed
                    font_thickness = 1
                    text_color = (255, 0, 0)
                    text = "RECORDING"
                    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
                    text_origin = (10, text_size[1] + 10)  # Top-left corner with padding

                    cv2.putText(frame, text, text_origin, font, font_scale, text_color, font_thickness)

                    if self.recording_out is None:  # Initialize the video writer
                        now = datetime.datetime.now()  # Get the current time
                        filename = now.strftime("%m-%d-%Y %H-%M-%S.mp4")  # Format the filename
                        filepath = os.path.join('recordings', filename)  # Add the 'recordings' folder to the path
                        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
                        self.recording_out = cv2.VideoWriter(filepath, fourcc, fps, (frame.shape[1], frame.shape[0])) 

                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert the frame to RGB color space
                    self.recording_out.write(frame_rgb)  # Write the RGB frame to the video file

            else:
                self.errorOccurred.emit("Error reading from camera")
                break

            self.imageUpdated.emit(image.copy())

    def calculate_fps(self):
        global start_time, frames 
        frames += 1
        elapsed_time = time.time() - start_time
        if elapsed_time > 1:  # Update FPS every second
            self.fps = frames / elapsed_time
            frames = 0
            start_time = time.time()
        return self.fps
    
    def start_recording(self):
        self.is_recording = True
        
    def stop_recording(self):
        self.is_recording = False
        if self.recording_out is not None:
            self.recording_out.release()
            self.recording_out = None

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.model_index = 0
        self.conf = 0.40
        self.iou = 0.50 
        self.models = self.getAvailableModels()  # list of models
        self.availableCameras = self.getAvailableCameras() #list of cameras
        self.maxID = self.maxIDFromDatabase()
        
        self.StartRecordButton.clicked.connect(self.toggle_recording)  # Connect the button
        
        # Add available cameras to the CameraSourceComboBox
        for item in self.availableCameras:
            if isinstance(item, int):
                self.CameraSourceComboBox.addItem(f"Camera {item+1}", item)
            elif isinstance(item, str):
                self.CameraSourceComboBox.addItem(item, item)

        # Connect the currentIndexChanged signal to the runInference method
        self.CameraSourceComboBox.currentIndexChanged.connect(self.runInference)

        self.advancedSettingsButton.clicked.connect(self.onAdvancedSettingsClicked)

        self.filterButton.clicked.connect(self.clickedFilterButton)

        self.updateDateEdits()

        self.runInference()

    def getAvailableCameras(self):
        available_cameras = []
        i = 0
        while True:
            cap = cv2.VideoCapture(i)
            if cap is None or not cap.isOpened():
                cap.release()
                break
            else:
                available_cameras.append(i)
                cap.release()
            i += 1
            available_cameras.append('rtsp://TAPOC200:TapoC200!@192.168.1.8:554/stream1')
        return available_cameras

    def getAvailableModels(self):
        # Get the directory of the current script
        directory = os.path.dirname(os.path.abspath(__file__))
        
        # Add the "models" subdirectory to the path
        models_directory = os.path.join(directory, 'models')
        
        # Return the full paths to the .pt files
        return [os.path.join(models_directory, f) for f in os.listdir(models_directory) if f.endswith('.pt')]

    def runInference(self):
        if hasattr(self, 'worker'):
            # Stop the current video capture and release the camera
            self.worker.imageUpdated.disconnect()
            self.worker.errorOccurred.disconnect()
            self.thread.quit()
            self.video_capture.release()

        # Start a new video capture with the selected camera
        self.current_camera_index = self.CameraSourceComboBox.currentData()
        self.video_capture = cv2.VideoCapture(self.current_camera_index)
        # self.video_capture = cv2.VideoCapture('rtsp://TAPOC200:TapoC200!@192.168.1.8:554/stream1')

        self.thread = QThread(self)
        self.worker = VideoWorker(self.video_capture, self.model_index, self.conf, self.iou, self.models, self.maxID)
        self.worker.moveToThread(self.thread)

        self.worker.imageUpdated.connect(self.update_frame)
        self.worker.objectListUpdated.connect(self.update_list_widget)
        self.worker.errorOccurred.connect(self.handle_error)
        self.thread.started.connect(self.worker.run)

        self.thread.start()

    def update_frame(self, image):
        pixmap = QPixmap.fromImage(image)
        scaled_pixmap = pixmap.scaled(self.VideoWidget.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  # Scale while keeping aspect ratio
        self.VideoWidget.setPixmap(scaled_pixmap)

    def update_list_widget(self, detected_objects):
        object_counts = {}
        for obj in detected_objects:
            object_name = obj[0]  # Extract the object name from the tuple
            object_counts[object_name] = object_counts.get(object_name, 0) + 1

        self.listWidget.clear()
        for obj, count in object_counts.items():
            self.listWidget.addItem(f"{obj} - {count}") 

        # Calculate and display total objects
        total_objects = sum(object_counts.values())
        self.totalObjectsDetectedNumber.setText(str(total_objects))

    def onAdvancedSettingsClicked(self):
        advancedSettings = settingsDialog(self, self.models, self.model_index, self.conf, self.iou)
        advancedSettings.modelChanged.connect(self.updateModel)
        if advancedSettings.exec():
            self.conf = advancedSettings.conf
            self.iou = advancedSettings.iou
            self.model_index = advancedSettings.AIModelComboBox.currentIndex()
            self.runInference()

    def updateModel(self, model_index):
        self.model_index = model_index

    def toggle_recording(self):
        if self.worker.is_recording:
            self.worker.stop_recording()
            self.StartRecordButton.setText("Start Recording")  # Update button text
        else:
            self.worker.start_recording()
            self.StartRecordButton.setText("Stop Recording")  # Update button text

    def maxIDFromDatabase(self):
        with Database() as database:
            self.max_id = database.selectMaxID()
        return self.max_id

    def updateDateEdits(self):
        with Database() as database:

            # Retrieve the earliest and latest dates
            earliest_date_str, latest_date_str = database.updateDateEdits()

            # Ensure that there are records in the database
            if earliest_date_str and latest_date_str:    
                # Assuming dateTime format is "MM-DD-YYYY HH-MM-SS"
                earliest_date = QDate.fromString(earliest_date_str.split(" ")[0], "MM-dd-yyyy")
                latest_date = QDate.fromString(latest_date_str.split(" ")[0], "MM-dd-yyyy")

                # Set the DateEdits
                self.fromDateEdit.setDate(earliest_date)
                self.fromDateEdit.setMinimumDate(earliest_date)
                self.fromDateEdit.setMaximumDate(latest_date)

                self.toDateEdit.setDate(latest_date)
                self.toDateEdit.setMaximumDate(latest_date)
                self.toDateEdit.setMinimumDate(earliest_date)

    def clickedFilterButton(self):
        with Database() as database:
            from_date = self.fromDateEdit.date().toString("MM-dd-yyyy")
            to_date = self.toDateEdit.date().addDays(1).toString("MM-dd-yyyy")

            # Calculate days between dates
            from_date_obj = datetime.datetime.strptime(from_date, "%M-%d-%Y").date()
            to_date_obj = datetime.datetime.strptime(to_date, "%M-%d-%Y").date()
            num_days = (to_date_obj - from_date_obj).days

            total_litter_count = database.count_rows_by_date_range(from_date, to_date)
            self.totalDetectedLitterLabel.setText(f"{total_litter_count}")

            if num_days > 0:  # Prevent division by zero
                average_daily_litter_count = total_litter_count / num_days
                self.averageDailyDetectedLitterLabel.setText(f"{average_daily_litter_count:.2f}")  # Format to 2 decimal places
            else:
                self.averageDailyDetectedLitterLabel.setText("Invalid date range")

            litter_data = database.litter_composition(from_date, to_date)
            self.totalRecyclableLitterLabel.setText(f"{litter_data['recyclable_percentage']:.2f}%")
            self.totalNonRecyclableLitterLabel.setText(f"{litter_data['non_recyclable_percentage']:.2f}%")

            recyclable_summary = database.litter_summary(from_date, to_date, True)
            self.recyclableLitterListWidget.clear()
            non_recyclable_summary = database.litter_summary(from_date, to_date, False)
            self.nonRecyclableLitterListWidget.clear()  # Clear the list widget

            for item in recyclable_summary:
                display_text = f"{item['className']} - {item['count']}"
                self.recyclableLitterListWidget.addItem(display_text)

            for item in non_recyclable_summary:
                display_text = f"{item['className']} - {item['count']}"
                self.nonRecyclableLitterListWidget.addItem(display_text)

    def handle_error(self, message):
        print(f"Error occurred: {message}")

    def closeEvent(self, event):
        self.worker.imageUpdated.disconnect()
        self.worker.errorOccurred.disconnect()
        self.thread.quit()
        self.video_capture.release()
        event.accept()

class settingsDialog(Ui_Dialog, QDialog):
    modelChanged = Signal(int)
    def __init__(self, parent=None, models=None, model_index=0, conf=0.40, iou=0.50):
        super().__init__(parent)
        self.setupUi(self)

        self.conf = conf
        self.iou = iou
        self.models = models if models is not None else []

        for model in self.models:
            self.AIModelComboBox.addItem(os.path.basename(model))

        self.AIModelComboBox.setCurrentIndex(model_index)

        # Set the range and initial value of the sliders
        self.ConfidenceThresholdHorizontalSlider.setRange(1, 100)
        self.ConfidenceThresholdHorizontalSlider.setValue(int(self.conf * 100))
        self.IoUThresholdHorizontalSlider.setRange(0, 95)
        self.IoUThresholdHorizontalSlider.setValue(int(self.iou * 100))

        # Set the initial text of the label to the value of conf and iou
        self.ConfidenceThresholdNumber.setText(str(self.conf))
        self.IoUThresholdNumber.setText(str(self.iou))

        # Connect the valueChanged signal to a slot
        self.ConfidenceThresholdHorizontalSlider.valueChanged.connect(self.updateConfidenceLabel)
        self.IoUThresholdHorizontalSlider.valueChanged.connect(self.updateIoULabel)

        # Connect the accepted signal to a slot
        self.buttonBox.accepted.connect(self.updateSliders)

    def updateConfidenceLabel(self, value):
        # Convert the value back to the range 0.01-1
        self.ConfidenceThresholdNumber.setText(str(value / 100))

    def updateIoULabel(self, value):
        # Convert the value back to the range 0-0.95
        self.IoUThresholdNumber.setText(str(value / 100))

    def updateSliders(self):
        # Update conf and iou to the current value of the sliders
        self.conf = self.ConfidenceThresholdHorizontalSlider.value() / 100
        self.iou = self.IoUThresholdHorizontalSlider.value() / 100

    def updateModel(self):
        self.modelChanged.emit(self.AIModelComboBox.currentIndex())

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()