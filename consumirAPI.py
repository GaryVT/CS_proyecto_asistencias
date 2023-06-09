from flask import Flask, jsonify
import requests
import json
import mysql.connector

app = Flask(__name__)

@app.route('/openfaceAPI')
def openface_api():
    # Realizar una solicitud HTTP al endpoint de OpenFace API
    response = requests.get('http://localhost:81/openfaceAPI')
    
    # Convertir la respuesta en un objeto Python
    data = json.loads(response.text)
    
    # Conectar a la base de datos MySQL
    cnx = mysql.connector.connect(user='usuario', password='contraseña',
                                   host='localhost',
                                   database='nombre_de_la_base_de_datos')
    
    # Obtener un cursor para ejecutar consultas SQL
    cursor = cnx.cursor()
    
    # Almacenar los vectores de características en la base de datos
    for vector in data['vectors']:
        add_vector = ("INSERT INTO caracteristicas "
                      "(vector) "
                      "VALUES (%s)")
        cursor.execute(add_vector, (json.dumps(vector),))
    
    # Guardar los cambios y cerrar la conexión a la base de datos
    cnx.commit()
    cursor.close()
    cnx.close()
    
    # Devolver una respuesta vacía
    return ""

if __name__ == '__main__':
    app.run(debug=True)