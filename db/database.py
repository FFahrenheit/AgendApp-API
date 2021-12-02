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
            self.cursor = self.connection.cursor()
        except Exception as e:
            print("No se pudo conectar a la base de datos")
            print(e)
            raise

    def agregar_usuario(self, correo, contraseña, nombre):
        if self.existe_usuario(correo):
            return False
        
        h = hashlib.new('sha256', bytes(contraseña,'utf-8'))
        h = h.hexdigest()
        query = "INSERT INTO usuario(correo, contraseña, nombre) VALUES (%s, %s, %s)"
        
        self.cursor.execute(query, (correo, h, nombre))
        self.connection.commit()

        return True

    def existe_usuario(self, correo):
        query = "SELECT COUNT(*) FROM usuario WHERE correo = %s"
        self.cursor.execute(query, (correo,))

        return self.cursor.fetchone()[0] == 1

    def iniciar_sesion(self, correo, contraseña):
        h = hashlib.new('sha256', bytes(contraseña, 'utf-8'))
        h = h.hexdigest()

        query = "SELECT id, nombre FROM usuario WHERE correo = %s AND contraseña = %s"
        self.cursor.execute(query, (correo, h))

        id = self.cursor.fetchone()

        if id:
            return id[0], id[1], True
        else:
            return None, None, False
