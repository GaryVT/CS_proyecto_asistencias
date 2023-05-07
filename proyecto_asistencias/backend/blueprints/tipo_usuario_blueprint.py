#de justificacion
#pip install psycopg2

from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.postgres_tipo_usuario_model import tipo_usuario_model

model = tipo_usuario_model()

tipo_usuario_blueprint = Blueprint('tipo_usuario_blueprint', __name__)

#################################################

@tipo_usuario_blueprint.route('/tipo_usuario', methods=['PUT'])
@cross_origin()
def crear_tipo_usuario():
    content = model.crear_tipo_usuario(request.json['nombre_tusr']) 
    return jsonify(content)

@tipo_usuario_blueprint.route('/tipo_usuario', methods=['PATCH'])
@cross_origin()
def actualizar_tipo_usuario():
    content = model.actualizar_tipo_usuario(request.json['tipousr_id']
                                            ,request.json['nombre_tusr'])    
    return jsonify(content)

@tipo_usuario_blueprint.route('/tipo_usuario', methods=['DELETE'])
@cross_origin()
def eliminar_tipo_usuario():
    return jsonify(model.eliminar_tipo_usuario(int(request.json['tipousr_id'])))

@tipo_usuario_blueprint.route('/tipo_usuarios', methods=['POST'])
@cross_origin()
def mostrar_tipo_usuarios():
    return jsonify(model.mostrar_tipo_usuarios())