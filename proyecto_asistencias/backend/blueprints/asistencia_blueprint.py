#de justificacion
#pip install psycopg2

from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.postgres_asistencia_model import AsistenciaModel

model = AsistenciaModel()

asistencia_blueprint = Blueprint('asistencia_blueprint', __name__)


@asistencia_blueprint.route('/asistencia', methods=['PUT'])
@cross_origin()
def crear_asistencia():
    content = model.crear_asistencia(request.json['fecha'],
                                 request.json['id_curso'],
                                 request.json['id_alumno'],
                                 request.json['presente'])    
    return jsonify(content)

@asistencia_blueprint.route('/asistencia', methods=['PATCH'])
@cross_origin()
def actualizar_asistencia():
    content = model.actualizar_asistencia(request.json['cod_asist'],request.json['fecha'],request.json['id_curso'],request.json['id_alumno'],request.json['presente'])    
    return jsonify(content)

@asistencia_blueprint.route('/asistencia', methods=['DELETE'])
@cross_origin()
def eliminar_asistencia():
    return jsonify(model.eliminar_asistencia(int(request.json['cod_asist'])))

@asistencia_blueprint.route('/asistencias', methods=['POST'])
@cross_origin()
def mostrar_asistencias():
    return jsonify(model.mostrar_asistencias())