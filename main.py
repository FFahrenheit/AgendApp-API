from flask import Flask, request
from flask.json import jsonify
from db.database import Database

def run_server():
    app = Flask(__name__)
    db = Database()

    @app.route('/api/v1/usuarios', methods = ['POST'])
    @app.route('/api/v1/usuarios/<int:id>/contactos', methods = ['GET'])
    def usuarios(id = None):
        if request.method == 'POST' and request.is_json:
            try:
                data = request.get_json()
                print(data)

                correo = data['correo']
                contraseña = data['contraseña']
                nombre = data['nombre']

                if(db.agregar_usuario(correo, contraseña, nombre)):
                    return jsonify(code = 'ok')
                else:
                    return jsonify(code = 'existe')

            except Exception as e:
                print(e)
                return jsonify(code = 'error')
        elif request.method == 'GET' and id is not None:
            return jsonify(db.get_contactos(id))

    @app.route('/api/v1/sesiones', methods = ['POST'])
    def sesiones():
        if request.method == 'POST' and request.is_json:
            try:
                data = request.get_json()
                correo = data['correo']
                contraseña = data['contraseña']

                id, nombre, ok = db.iniciar_sesion(correo, contraseña)

                if ok:
                    return jsonify(code = 'ok', id = id, nombre = nombre)
                else:
                    return jsonify(code = 'no')
            except Exception as e:
                print(e)
                return jsonify(code = 'error')

    @app.route('/api/v1/contactos', methods = ['POST'])
    @app.route('/api/v1/contactos/<int:id>', methods = ['GET', 'DELETE', 'PATCH'])
    def contactos(id = None):
        if request.method == 'POST' and request.is_json:
            try:
                data = request.get_json()
                print(data)

                if db.agregar_contacto(data):
                    return jsonify(code = 'ok')
                else:
                    return jsonify(code = 'no')
            except Exception as e:
                print(e)
                return jsonify(code = 'error')
        elif id is not None:
            if request.method == 'GET':
                return jsonify(db.detalles_contacto(id))
            elif request.method == 'DELETE':
                if db.eliminar_contacto(id):
                    return jsonify(code = 'ok')
                else:
                    return jsonify(code = 'error')
            elif request.method == 'PATCH' and request.is_json:
                data = request.get_json()
                columna = data['columna']
                valor = data['valor']
                
                if db.modificar_contacto(id, columna, valor):
                    return jsonify(code = 'ok')
                else:
                    return jsonify(code = 'error')

    app.run(debug = True)

if __name__ == '__main__':
    run_server()