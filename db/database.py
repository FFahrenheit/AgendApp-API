import mysql.connector
import hashlib

class Database:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                user = 'agendapp_admin',
                password = 'AgendApp',
                database = 'agendapp'
            )
        except:
            print("No se pudo conectar a la base de datos")
            raise