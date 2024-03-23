from PySide6.QtSql import QSqlDatabase, QSqlQuery

class Database():
    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("database")

    def __enter__(self):
        self.db.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()

    def createObjectsTable(self):
        createTableQuery = QSqlQuery()
        createTableQuery.exec(
            """
            CREATE TABLE objects (
                objectID INTEGER PRIMARY KEY UNIQUE NOT NULL,
                className TEXT NOT NULL,
                confidenceLevel REAL NOT NULL,
                recyclableBool INTEGER NOT NULL,
                dateTime TEXT NOT NULL
            )
            """
        )

    def createAlertsTable(self):
        createTableQuery = QSqlQuery()
        createTableQuery.exec(
            """
            CREATE TABLE alerts (
                className TEXT PRIMARY KEY UNIQUE NOT NULL,
                alertAmount INTEGER NOT NULL
            )
            """
        )

    def dropTable(self):
        createTableQuery = QSqlQuery()
        createTableQuery.exec(
            """
            DROP TABLE alerts
            """
        )
    
    def insertObject(self, objectID, className, confidenceLevel, recyclableBool, dateTime):
        query = QSqlQuery()
        query.prepare(
            "INSERT INTO objects (objectID, className, confidenceLevel, recyclableBool, dateTime)"
            "VALUES (?, ?, ?, ?, ?)"
        )
        query.addBindValue(objectID)
        query.addBindValue(className)
        query.addBindValue(confidenceLevel)
        query.addBindValue(recyclableBool)
        query.addBindValue(dateTime)

        #Parameterization - to prevent SQL injection vulnerabilities
        if not query.exec_():
            print(f"Error inserting object: {query.lastError().text()}")

    def insertAlert(self, className, alertAmount):
        query = QSqlQuery()
        query.prepare(
            "INSERT INTO alerts (className, alertAmount) "
            "VALUES (?, ?)"
        )
        query.addBindValue(className)
        query.addBindValue(alertAmount)

        #Parameterization - to prevent SQL injection vulnerabilities
        if not query.exec_():
            print(f"Error inserting object: {query.lastError().text()}")
            
    def removeAlert(self, className):
        query = QSqlQuery()
        query.prepare(
            "DELETE FROM alerts WHERE className = ?"
        )
        query.addBindValue(className)

        if not query.exec_():
            print(f"Error deleting object: {query.lastError().text()}")

    def selectAllObjects(self):
        query = QSqlQuery()
        query.exec(
        """
        SELECT * FROM objects
        """
        )

        while query.next():
            print(query.value("objectID"), query.value("className"), query.value("confidenceLevel"), query.value("recyclableBool"), query.value("dateTime"))

    def selectAllAlerts(self):
        query = QSqlQuery()
        query.exec(
        """
        SELECT * FROM alerts
        """
        )

        alerts = []
        while query.next():
            item_name = query.value("className")
            amount = query.value("alertAmount")
            alerts.append((item_name, amount))

        return alerts

    def truncateTable(self):
        self.db.open()

        query = QSqlQuery()
        query.exec(
            """
            DELETE FROM alerts
            """
        )

        if not query.isActive():
            print(f"Error truncating table: {query.lastError().text()}")

    def selectMaxID(self):
        query = QSqlQuery()
        query.exec(
        """
        SELECT MAX(objectID) FROM objects
        """
        )

        if query.next():
            max_id = query.value(0)

        return max_id
    
    def updateDateEdits(self):  # Add 'self' as the method belongs to a class
        query = QSqlQuery()
        # Retrieve the earliest and latest dates
        query.exec(
        """
        SELECT MIN(dateTime), MAX(dateTime) FROM objects
        """
        )

        # Fetch results and return
        query.next()  # Move to first row
        earliest_date_str = query.value(0)
        latest_date_str = query.value(1)

        return earliest_date_str, latest_date_str 

    def count_rows_by_date_range(self, from_date, to_date):
        query = QSqlQuery()
        query.prepare(
        """
        SELECT COUNT(*) FROM objects WHERE dateTime BETWEEN :from_date AND :to_date
        """)
        query.bindValue(":from_date", from_date)
        query.bindValue(":to_date", to_date)
        query.exec()
        query.next()

        return query.value(0)
    
    def average_daily_detected_litter(self, from_date, to_date):
        query = QSqlQuery()
        query.prepare("SELECT SUM(count) as total_count, COUNT(DISTINCT DATE(dateTime)) as num_days FROM (SELECT COUNT(*) as count, DATE(dateTime) as date FROM objects WHERE dateTime BETWEEN :from_date AND :to_date GROUP BY date)")
        query.bindValue(":from_date", from_date)
        query.bindValue(":to_date", to_date)
        query.exec()
        query.next() 

        total_count = query.value(0)
        num_days = query.value(1)

        if num_days > 0:
            return total_count / num_days
        else:
            return None  # Or handle the case of no data in the range
        
    def litter_composition(self, from_date, to_date):
        query = QSqlQuery()
        query.prepare("""
            SELECT 
                SUM(CASE WHEN recyclableBool = 1 THEN 1 ELSE 0 END) as recyclable_count,
                SUM(CASE WHEN recyclableBool = 0 THEN 1 ELSE 0 END) as non_recyclable_count,
                COUNT(*) as total_count 
            FROM objects 
            WHERE dateTime BETWEEN :from_date AND :to_date
        """)
        query.bindValue(":from_date", from_date)
        query.bindValue(":to_date", to_date)
        query.exec()
        query.next() 

        recyclable_count = query.value(0)
        non_recyclable_count = query.value(1)
        total_count = query.value(2)

        if total_count > 0:
            return {
                "recyclable_percentage": (recyclable_count / total_count) * 100,
                "non_recyclable_percentage": (non_recyclable_count / total_count) * 100
            }
        else:
            return None  # Or handle the case of no data in the range

    def litter_summary(self, from_date, to_date, recyclable):
        query = QSqlQuery()
        query.prepare("""
            SELECT className, COUNT(*) as count 
            FROM objects 
            WHERE recyclableBool = :recyclable AND dateTime BETWEEN :from_date AND :to_date
            GROUP BY className
        """)
        query.bindValue(":from_date", from_date)
        query.bindValue(":to_date", to_date)
        query.bindValue(":recyclable", 1 if recyclable else 0)  # Bind 1 for recyclable, 0 otherwise
        query.exec()
    
        litter_summary = []
        while query.next():
            className = query.value(0)
            count = query.value(1)
            litter_summary.append({"className": className, "count": count})

        return litter_summary 

    def detected_litter_per_day(self, from_date, to_date):
        query = QSqlQuery()
        query.prepare("SELECT dateTime, COUNT(*) as count FROM objects WHERE dateTime BETWEEN :from_date AND :to_date GROUP BY substr(dateTime, 1, 10)")
        query.bindValue(":from_date", from_date)
        query.bindValue(":to_date", to_date)
        query.exec()

        result = []
        while query.next():
            date_time = query.value(0)
            count = query.value(1)
            date = date_time.split(" ")[0]  # Extract the date part from the dateTime string
            date = "-".join(date.split("-")[:2])  # Omit the year
            result.append({'date': date, 'count': str(count)})

        return result
    
    def count_class_names(self, from_date, to_date):
        query = QSqlQuery()
        query.prepare("SELECT className, COUNT(*) as count FROM objects WHERE dateTime BETWEEN :from_date AND :to_date GROUP BY className")
        query.bindValue(":from_date", from_date)
        query.bindValue(":to_date", to_date)
        query.exec()

        result = []
        while query.next():
            class_name = query.value(0)
            count = query.value(1)
            result.append({class_name: str(count)})

        return result
    
    def get_class_percentages(self, from_date, to_date):
        # First, get the total count of objects within the date range
        total_count = self.count_rows_by_date_range(from_date, to_date)

        query = QSqlQuery()
        query.prepare("SELECT className, COUNT(*) as count FROM objects WHERE dateTime BETWEEN :from_date AND :to_date GROUP BY className")
        query.bindValue(":from_date", from_date)
        query.bindValue(":to_date", to_date)
        query.exec()

        result = []
        while query.next():
            class_name = query.value(0)
            count = query.value(1)
            # Calculate the percentage and round it to 2 decimal places
            percentage = round((count / total_count) * 100, 2)
            result.append({class_name: str(percentage) + '%'})

        return result





