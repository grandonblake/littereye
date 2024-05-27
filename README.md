# littereye
LitterEye: Automated and Real-Time Litter Detection System using YOLOv8

It is an automated and real-time litter detection system using the YOLOv8m model. The system is made with PySide6 and can be connected to a CCTV camera using OpenCV.

This project was a group effort that was submitted on May 21, 2024 as our Thesis during my 4th year in College.

## Abstract
In urban areas, effective litter management is crucial for maintaining cleanliness and public health. This study aims to develop a real-time litter detection system utilizing the YOLOv8 model, focusing on training the model to detect street litter. The importance of this study lies in its potential to enhance waste management practices. By providing real-time data on litter type and amount, this system can help local governments, recycling organizations, and communities manage waste faster and more effectively, contributing to cleaner urban environments and improved public health. The methodology involved capturing and annotating images of street litter to create a custom dataset, combined with the TACO dataset. The YOLOv8 model was trained using this comprehensive dataset, with performance evaluated through metrics such as Precision, Recall, F1 score, and mean Average Precision (mAP). The system was developed using the PySide6 framework and integrated with live video feeds via the OpenCV library, assessed based on ISO/IEC 25010 software quality standards. The YOLOv8 model achieved an mAP50 of 91.63% and mAP50-95 of 76.59%, with a precision of 91.27% and a recall of 88.13%, demonstrating its effectiveness. The system received positive feedback, with a high overall satisfaction rating of 4.29 for functional suitability, performance efficiency, and usability. In conclusion, this study develops a successful real-time litter detection system, significantly contributing to waste management literature and practices. The system's practical implications include improved waste monitoring for citizens, businesses, local governments, and recycling organizations, fostering a cleaner and more sustainable urban environment.

## Objectives
This study aims to develop a system that can detect street litter by utilizing the YOLOv8 model in real-time object detection. Specifically, the study aims to:

 - Train a YOLOv8 model to be able to detect street litter;
 - Develop an object detection system integrating the trained YOLOv8 model that is capable of detecting litter in real-time;
 - Measure the performance of the trained model in terms of Precision, Recall, F1 score, confusion matrix, learning curves, and get the overall performance using the mean Average Precision (mAP);
 - Evaluate the system using ISO/IEC 25010 - software product quality standard in terms of (1) Functional Suitability, (2) Performance Efficiency, and (3) Usability.

## Scope and Delimitations
This study explores the theoretical basis and real-world applications of utilizing cutting-edge computer vision algorithms for the significant problem of detecting and managing waste. It seeks to contribute to the exploration of object detection systems with a particular focus on detecting street litter or waste. The primary goal is to utilize an object detection model to be able to develop a system that will be able to detect street litter in real-time.

The study will focus on training a YOLOv8 model that will be able to detect street litter. This includes understanding the principles behind the YOLOv8 model, its application in object detection, and its potential for detecting street litter. The training of the model will utilize datasets that were captured by the researchers and from online sources. Additionally, it involves utilizing the trained YOLOv8 model and developing a system that will be able to detect street litter in real-time using a camera or video source. With this, the users will be able to record the video within the system for possible future review. Furthermore, the system will provide a summary report of the litter detected by the system which would also include their classification whether they are recyclable or not.

This study centers on the exploration of the YOLOv8 model as an object detection system for street litter. The system would only be able to detect objects that are part of the dataset used to train the object detection model. It will only focus on the detection of street litter and will not address the physical collection or disposal of the detected litter. While the focus is on street litter, the technology could potentially be adapted to detect litter in other settings (e.g., parks, rivers) with further dataset development. Also, the initial images in the dataset are taken in the day which might make it difficult for detection in the night or in dark places. Additionally, the system cannot determine whether a specific object is considered a waste/litter or not. It also does not directly address the root causes of littering behavior or explore the broader social and environmental implications of waste management. Furthermore, there would only be one live video feed shown from a chosen camera at a time. The CCTV camera that the researchers utilized for this study is the TAPO C200. The summary report will only provide a summary of the detected litter, it will not provide recommendations or analysis of the litter.

## Conceptual Framework (IPO diagram)
<img src="/screenshots/conceptualframework.png" width=75% height=75%>

The conceptual framework details the input-process-output (IPO) diagram of the whole study. The input of the study begins by combining a dataset for training that is composed of the researcher’s captured litter images and the TACO dataset. Afterwards, the process of the study involves steps that are necessary to prepare the data for training the model. This includes data annotation, data preprocessing, and data augmentation. Then, the process of training the YOLOv8 model can be done on the augmented combined dataset. The output of the study involves steps needed to be done after training the model, this includes evaluating the model and getting it ready to detect street litter in real-time. The model needs to be evaluated via the mean Average Precision (mAP), precision, recall, F1 score, confusion matrix, and learning curve. These metrics determine how the model performed against the validation set and how the model will perform on new and unseen images. Additionally, it will help decide whether the model needs further training, if the hyperparameters of training the model needs to be altered, or if the dataset on training the model needs to be increased or improved. Then, after evaluating the model, it can now be deployed to detect litters on the street using real-time video footage and the result will be saved in the database and outputted in the screen of the system. If a litter’s threshold is exceeded, it will then send a notification on the screen of the system.

## System Architecture
<img src="/screenshots/systemarchitecture.png" width=75% height=75%>

The system architecture is structured into three key tiers: Presentation, Logic, and Data. In the Presentation tier, a camera will capture real-time footage of unknown detected objects and pass it to the system for identification. It will then transition to the Logic tier, on which the unknown detected object will be identified by the YOLOv8 model through its backbone, neck, and head. Afterwards, the amount and the class of the detected object will be determined which will be known as the results. Then, the results, which is the amount and the type of the detected object, will be saved to the database in the Data tier. Simultaneously, the results of the detected object will also be displayed on the screen of the system in the Presentation tier.

## Street Litter that can be detected
<img src="/screenshots/streetlitterdetected.jpg" width=50% height=50%>

## System screenshots
<img src="/screenshots/detecttab.jpg" width=75% height=75%>
<img src="/screenshots/camerasettings.jpg" width=50% height=50%>
<img src="/screenshots/setalert.jpg" width=50% height=50%>
<img src="/screenshots/advancedsettings.jpg" width=25% height=25%>
<img src="/screenshots/summaryreport.jpg" width=75% height=75%>
<img src="/screenshots/printpreview.jpg" width=75% height=75%>



