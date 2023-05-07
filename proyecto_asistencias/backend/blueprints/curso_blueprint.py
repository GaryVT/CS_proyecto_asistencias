from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename

import json
from flask_cors import CORS, cross_origin 

from backend.models.postgres_curso_model import CursoModel
model = CursoModel()

curso_blueprint = Blueprint('curso_blueprint', __name__)


@curso_blueprint.route('/curso', methods=['PUT'])
@cross_origin()
def crear_curso():
    content = model.crear_curso(request.json['id_docente'],request.json['nombre_curso'],request.json['descripcion'])    
    return jsonify(content)

@curso_blueprint.route('/curso', methods=['PATCH'])
@cross_origin()
def actualizar_curso():
    content = model.actualizar_curso(request.json['id_curso'],request.json['id_docente'],request.json['nombre_curso'],request.json['descripcion'])    
    return jsonify(content)

@curso_blueprint.route('/curso', methods=['DELETE'])
@cross_origin()
def eliminar_curso():
    return jsonify(model.eliminar_curso(int(request.json['id_curso'])))

@curso_blueprint.route('/cursos', methods=['POST'])
@cross_origin()
def mostrar_cursos():
    return jsonify(model.mostrar_cursos())