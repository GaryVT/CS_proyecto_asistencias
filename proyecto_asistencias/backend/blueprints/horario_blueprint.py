#de justificacion
#pip install psycopg2

from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.postgres_horario_model import HorarioModel

model = HorarioModel()

horario_blueprint = Blueprint('horario_blueprint', __name__)


@horario_blueprint.route('/horario', methods=['PUT'])
@cross_origin()
def crear_horario():
    content = model.crear_horario(request.json['id_curso'],
                                 request.json['hora_inicio'],
                                 request.json['hora_fin'],
                                 request.json['dia'],
                                 request.json['aula'])    
    return jsonify(content)

@horario_blueprint.route('/horario', methods=['PATCH'])
@cross_origin()
def actualizar_horario():
    content = model.actualizar_horario(request.json['id_horario'],request.json['id_curso'],request.json['hora_inicio'],request.json['hora_fin'],request.json['dia'],request.json['aula'])    
    return jsonify(content)

@horario_blueprint.route('/horario', methods=['DELETE'])
@cross_origin()
def eliminar_horario():
    return jsonify(model.eliminar_horario(int(request.json['id_horario'])))

@horario_blueprint.route('/horarios', methods=['POST'])
@cross_origin()
def mostrar_horarios():
    return jsonify(model.mostrar_horarios())