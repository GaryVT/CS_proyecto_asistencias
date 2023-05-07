#pip install psycopg2
from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
import requests
import os
import json
import numpy as np
from flask_cors import CORS, cross_origin 
import re
import html

from backend.blueprints.funciones import transformarResultado, euclidianaDistance
from backend.blueprints.funciones import *

#from backend.models.mysql_user_model import UserModel
#model = UserModel()


from backend.models.postgres_usuario_model import UsuarioModel

model = UsuarioModel()


usuario_blueprint = Blueprint('usuario_blueprint', __name__)

#################################################

@usuario_blueprint.route('/test', methods=['POST'])
# @wrap('decorator')
def test():
    if request.method == 'POST':
        f = request.files['file']
        data = request.form.get('data')
        #data=json.loads(request.form.get('data'))
        
        # si queremos guardar la foto
        filename = f.filename
        #path = "E://LaSalle//2022-II//ConstruccionSoftware//Parcial//img" + filename
        path = "C://Users//Usuario//Desktop//Ejemplo//proyecto_asistencias//Fotos//" + filename
        
        
        f.save(path)       
        

        # call openfaceAPI ##################################
        #url = 'http://127.0.0.1:81/openfaceAPI'
        url = 'http://localhost:81/openfaceAPI'
        files = {'file': open(path, 'rb')}
        #files = {'file': f}

        result = requests.post(url, files=files)
        result = result.json()



        
        ##-----------------------------------------Coge vector2 = vector que genera a partir de la imagen
        
        #vector = model.obtener_foto(int(data))
        vector = (result)
        #print(type(vector))
        vector = dictToString(vector)
        #print("vector con funcion tostring", type(vector))
        vector=toFloat(vector)
        #print("vector con funcion tofloat", type(vector))
        #print(vector)
        


        ##------------------------------------------Coge vector1 == vector del sistema

        vector_db = model.obtener_foto(int(data))
        
        vector_db = dictToString(vector_db)
        vector_db=toFloat(vector_db)

        ##-----------------------------------------Hallando la distancia euclidiana

        vector = np.array(vector)

        vector_db = np.array(vector_db)

        print("--------------------------------------------------------------")

    
        if isinstance(vector_db, np.ndarray):
            print("La variable es un numpy.ndarray")
            print("vector_db")
            print(vector_db.size)
            print(vector_db)


        if isinstance(vector, np.ndarray):
            print("La variable es un numpy.ndarray")
            print("vector")
            print(vector.size)
            print(vector)
        
        #arreglo1 = texto_con_salto.split()
        #arreglo2 = vector_db.split()
        print("arreglo1 Distancia Euclidiana:")
        #arreglo1 = np.fromstring(texto_con_salto, dtype=float, sep=' ')
        #arreglo2 = np.fromstring(vector_db, dtype=float, sep=' ')

        #arreglo1 = eval(texto_con_salto)
        #arreglo2 = eval(vector_db)

        #arreglo1 = texto_con_salto.astype(float)
        #arreglo2 = vector_db.astype(float)
        #print(arreglo1)
        #print(arreglo2)
        Edistancia = np.linalg.norm(vector - vector_db)
        #Edistancia = euclidianaDistance(vector, vector_db)

        print(Edistancia)#9 o 11
        
        #print(euclidianaDistance(vector_db, vector))
        '''if vector_db == vector:
            print("Los strings son iguales")
        else:
            print("Los strings son diferentes")'''
        
        ######################################################
       
        # queda pendiente: registrar los demas datas del 
        # usuario en la BD junto con el vector de caracteristicas
       
        #string = listToString(result)
        #print(result)

    return jsonify(result)


##################################################

@usuario_blueprint.route('/user', methods=['PUT'])
@cross_origin()
def crear_usuario():
    #f = requests.files['file']
    #filename = f.filename
    #f.save("C://Users//Usuario//Desktop//Ejemplo//proyecto_asistencias//Fotos/" + filename)
    #f_save = ("C://Users//Usuario//Desktop//Ejemplo//proyecto_asistencias//Fotos/" + filename )

    content = model.crear_usuario(request.json['dni']
                                  ,request.json['contrasena']
                                  ,request.json['nombre']
                                  ,request.json['apellido']
                                  ,request.json['tipousuario']
                                  ,request.json['fotoSistema']) 
    #data = {"foto":f_save}
    #response = requests.put('http://127.0.0.1:5050/user',json=data)

    return jsonify(content)

@usuario_blueprint.route('/user', methods=['PATCH'])
@cross_origin()
def actualizar_usuario():
    content = model.actualizar_usuario(request.json['id_usuario']
                                       ,request.json['dni']
                                       ,request.json['contrasena']
                                       ,request.json['nombre']
                                       ,request.json['apellido']
                                       ,request.json['tipousuario'])   
    return jsonify(content)

@usuario_blueprint.route('/user', methods=['DELETE'])
@cross_origin()
def eliminar_usuario():
    return jsonify(model.eliminar_usuario(int(request.json['id_usuario'])))

@usuario_blueprint.route('/users', methods=['POST'])
@cross_origin()
def mostrar_usuarios():
    return jsonify(model.mostrar_usuarios())

@usuario_blueprint.route('/user/foto_sistema', methods=['POST'])
@cross_origin()
def obtener_foto():
     return jsonify(model.obtener_foto(int(request.json['id_usuario'])))