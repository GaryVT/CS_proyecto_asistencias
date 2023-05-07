#de justificacion
#pip install psycopg2

from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.postgres_docente_model import docenteModel

model = docenteModel()

docente_blueprint = Blueprint('docente_blueprint', __name__)


@docente_blueprint.route('/docente', methods=['PUT'])
@cross_origin()
def crear_docente():
    content = model.crear_docente(request.json['id_usuario'],
                                 request.json['tipousr_id'],
                                 request.json['tipo_docente'])    
    return jsonify(content)

@docente_blueprint.route('/docente', methods=['PATCH'])
@cross_origin()
def actualizar_docente():
    content = model.actualizar_docente(request.json['id_docente'],request.json['id_usuario'],request.json['tipousr_id'],request.json['tipo_docente'])    
    return jsonify(content)

@docente_blueprint.route('/docente', methods=['DELETE'])
@cross_origin()
def eliminar_docente():
    return jsonify(model.eliminar_docente(int(request.json['id_docente'])))

@docente_blueprint.route('/docentes', methods=['POST'])
@cross_origin()
def mostrar_docentes():
    return jsonify(model.mostrar_docentes())