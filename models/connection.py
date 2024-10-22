import mysql.connector

class Connection:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="127.0.0.1",
                port=3306,
                user="root",
                password="root",
                database="todo"
            )
            self.cursor = self.connection.cursor()
            print("Connection successful:", self.connection)
        except Exception as err:
            print(f"Error: {err}")

    def close_connection(self):
        self.cursor.close()
        self.connection.close()


