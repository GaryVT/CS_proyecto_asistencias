from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_cors import CORS, cross_origin 

from backend.blueprints.usuario_blueprint import usuario_blueprint
from backend.blueprints.tipo_usuario_blueprint import tipo_usuario_blueprint
from backend.blueprints.alumno_blueprint import alumno_blueprint
from backend.blueprints.docente_blueprint import docente_blueprint
from backend.blueprints.curso_blueprint import curso_blueprint
from backend.blueprints.horario_blueprint import horario_blueprint
from backend.blueprints.matricula_blueprint import matricula_blueprint
from backend.blueprints.participacion_blueprint import participacion_blueprint
from backend.blueprints.asistencia_blueprint import asistencia_blueprint
from backend.blueprints.justificacion_blueprint import justificacion_blueprint

app = Flask(__name__)

app.register_blueprint(usuario_blueprint)
app.register_blueprint(tipo_usuario_blueprint)
app.register_blueprint(alumno_blueprint)
app.register_blueprint(docente_blueprint)
app.register_blueprint(curso_blueprint)
app.register_blueprint(horario_blueprint)
app.register_blueprint(matricula_blueprint)
app.register_blueprint(participacion_blueprint)
app.register_blueprint(asistencia_blueprint)
app.register_blueprint(justificacion_blueprint)


cors = CORS(app)

if __name__ == "__main__":
    app.run(debug=True, port=5050)