#de justificacion
#pip install psycopg2

from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.postgres_justificacion_model import JustificacionModel

model = JustificacionModel()

justificacion_blueprint = Blueprint('justificacion_blueprint', __name__)


@justificacion_blueprint.route('/justificacion', methods=['PUT'])
@cross_origin()
def crear_justificacion():
    content = model.crear_justificacion(request.json['cod_asist'],
                                 request.json['fecha'],
                                 request.json['descrip'])    
    return jsonify(content)

@justificacion_blueprint.route('/justificacion', methods=['PATCH'])
@cross_origin()
def actualizar_justificacion():
    content = model.actualizar_justificacion(request.json['cod_justi'],request.json['cod_asist'],request.json['fecha'],request.json['descrip'])    
    return jsonify(content)

@justificacion_blueprint.route('/justificacion', methods=['DELETE'])
@cross_origin()
def eliminar_justificacion():
    return jsonify(model.eliminar_justificacion(int(request.json['cod_justi'])))

@justificacion_blueprint.route('/justificaciones', methods=['POST'])
@cross_origin()
def mostrar_justificaciones():
    return jsonify(model.mostrar_justificaciones())