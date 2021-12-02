from flask import Flask, request
from flask.json import jsonify
from db.database import Database

def run_server():
    app = Flask(__name__)
    db = Database()

    @app.route('/api/v1/usuarios', methods = ['POST'])
    def usuarios():
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
            
    app.run(debug = True)

if __name__ == '__main__':
    run_server()