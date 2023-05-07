#de justificacion
#pip install psycopg2

from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.postgres_matricula_model import MatriculaModel

model = MatriculaModel()

matricula_blueprint = Blueprint('matricula_blueprint', __name__)

@matricula_blueprint.route('/matricula', methods=['PUT'])
@cross_origin()
def crear_matricula():
    content = model.crear_matricula(request.json['id_alumno'],
                                 request.json['id_curso'],
                                 request.json['fecha_matricula'],
                                 request.json['estado_matricula'])    
    return jsonify(content)

@matricula_blueprint.route('/matricula', methods=['PATCH'])
@cross_origin()
def actualizar_matricula():
    content = model.actualizar_matricula(request.json['matricula_id'],request.json['id_alumno'],request.json['id_curso'],request.json['fecha_matricula'],request.json['estado_matricula'])    
    return jsonify(content)

@matricula_blueprint.route('/matricula', methods=['DELETE'])
@cross_origin()
def eliminar_matricula():
    return jsonify(model.eliminar_matricula(int(request.json['matricula_id'])))

@matricula_blueprint.route('/matriculas', methods=['POST'])
@cross_origin()
def mostrar_matriculas():
    return jsonify(model.mostrar_matriculas())