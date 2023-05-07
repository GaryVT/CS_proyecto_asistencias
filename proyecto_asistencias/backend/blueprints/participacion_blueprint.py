#de justificacion
#pip install psycopg2

from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.postgres_participacion_model import ParticipacionModel

model = ParticipacionModel()

participacion_blueprint = Blueprint('participacion_blueprint', __name__)


@participacion_blueprint.route('/participacion', methods=['PUT'])
@cross_origin()
def crear_participacion():
    content = model.crear_participacion(request.json['part_fecha'],
                                 request.json['id_curso'],
                                 request.json['id_alumno'],
                                 request.json['cantidad'])    
    return jsonify(content)

@participacion_blueprint.route('/participacion', methods=['PATCH'])
@cross_origin()
def actualizar_participacion():
    content = model.actualizar_participacion(request.json['part_id'],request.json['part_fecha'],request.json['id_curso'],request.json['id_alumno'],request.json['cantidad'])    
    return jsonify(content)

@participacion_blueprint.route('/participacion', methods=['DELETE'])
@cross_origin()
def eliminar_participacion():
    return jsonify(model.eliminar_participacion(int(request.json['part_id'])))

@participacion_blueprint.route('/participaciones', methods=['POST'])
@cross_origin()
def mostrar_participaciones():
    return jsonify(model.mostrar_participaciones())