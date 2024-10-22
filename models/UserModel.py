import models.connection as conn

class UserModel:
    def __init__(self):
        self.oConn = conn.Connection()

    def insertUser(self, sName, sEmail,sTask):
        try:
            sQuery = "INSERT INTO users (name, email,task) VALUES (%s, %s,%s)"
            values = (sName, sEmail,sTask)
            self.oConn.cursor.execute(sQuery, values)
            self.oConn.connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def updateUser(self, sName, sEmail,sTask, iID):
        try:
            updates = []
            if sName:
                updates.append(f"name = %s")
            if sEmail:
                updates.append(f"email = %s")
            if sTask:
                updates.append(f"task = %s")

            sQuery = f"UPDATE users SET {', '.join(updates)} WHERE id = %s"
            values = ([sName, sEmail,sTask] + [iID])
            self.oConn.cursor.execute(sQuery, values)
            self.oConn.connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def deleteUser(self, iID):
        try:
            sQuery = "UPDATE users SET deleted = 1 WHERE id = %s"
            self.oConn.cursor.execute(sQuery, (iID,))
            self.oConn.connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def fetchAllUsers(self):
        try:
            sQuery = "SELECT * FROM users where deleted = 0"
            self.oConn.cursor.execute(sQuery)
            users = self.oConn.cursor.fetchall()
            return users
        except Exception as e:
            print(f"Error: {e}")
            return None

    def fetchUserById(self, iID):
        try:

            sQuery = "SELECT * FROM users WHERE id = %s"
            self.oConn.cursor.execute(sQuery, (iID,))
            user = self.oConn.cursor.fetchone()
            return user
        except Exception as e:
            print(f"Error: {e}")
            return None
