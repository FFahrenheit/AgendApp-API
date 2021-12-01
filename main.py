from flask import Flask
from db.database import Database

def run_server():
    app = Flask(__name__)
    bd = Database()

    app.run(debug = True)
    
if __name__ == '__main__':
    run_server()