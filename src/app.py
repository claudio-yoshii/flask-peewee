from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from db_conn import mysql
from resources.usuario import Usuarios
from resources.veiculos import Veiculos

app = Flask(__name__)

CORS(app)

api = Api(app)

db = mysql.init(app)

api.add_resource(Usuarios, '/usuarios', resource_class_kwargs={'db': db})

api.add_resource(Veiculos, '/veiculos', resource_class_kwargs={'db': db})

if __name__ == '__main__':
    app.run()
