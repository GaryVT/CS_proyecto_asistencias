#de justificacion
#pip install psycopg2

from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.postgres_alumno_model import AlumnoModel

model = AlumnoModel()

alumno_blueprint = Blueprint('alumno_blueprint', __name__)


@alumno_blueprint.route('/alumno', methods=['PUT'])
@cross_origin()
def crear_alumno():
    content = model.crear_alumno(request.json['id_usuario'],
                                 request.json['tipousr_id'],
                                 request.json['anio_alumno'],
                                 request.json['carrera'])    
    return jsonify(content)

@alumno_blueprint.route('/alumno', methods=['PATCH'])
@cross_origin()
def actualizar_alumno():
    content = model.actualizar_alumno(request.json['id_alumno'],request.json['id_usuario'],request.json['tipousr_id'],request.json['anio_alumno'],request.json['carrera'])    
    return jsonify(content)

@alumno_blueprint.route('/alumno', methods=['DELETE'])
@cross_origin()
def eliminar_alumno():
    return jsonify(model.eliminar_alumno(int(request.json['id_alumno'])))

@alumno_blueprint.route('/alumnos', methods=['POST'])
@cross_origin()
def mostrar_alumnos():
    return jsonify(model.mostrar_alumnos())