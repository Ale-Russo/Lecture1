import mysql.connector


class DBConnect:

    @classmethod
    def getConnection(self):

        try:
            cnx=mysql.connector.connect(
                user = "root",
                password = "1234",
                host = "127.0.0.1",
                database = "sw_gestionale"
            )
            return cnx
        except mysql.connector.Error as err:
            print("Non riesco a collegarmi al DB")
            print(err)
            return None