import numpy as np
import requests
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




def toString(result):
    res = []
    # Eliminar los corchetes "[" y "]" de la cadena
    result = result.replace('[', '').replace(']', '').replace('{', '').replace('}', '')

    # Dividir la cadena en una lista de elementos individuales
    result = result.split()

    #result = list(result.split(' ')) 
   
    for i in result:
        if i == '':
            pass
        else:
            res.append(i)
   
    return res


# Convert String list to Float list 
# Return Float list
def stringToFloat(arr):
    vector = []
    for i in arr:
        vector.append(float(i))

    return vector


# Calculate Euclidean distance
# Return Float
def euclidianaDistance(vector1, vector2):
    dist = np.sqrt(np.sum(np.square(vector1 - vector2)))
    return dist




# Convert Dictionary to String
# Return string list 
def transformarResultado(result):
    vector = []
    #result = result['result'].replace("\n", "").replace("  ", " ").replace("[", "").replace("]", "") 
        
    # Eliminar los corchetes "[" y "]" de la cadena
    result = result.replace('[', '').replace(']', '').replace('{', '').replace('}', '')

    # Dividir la cadena en una lista de elementos individuales
    elementos = result.split()

    # Convertir cada elemento en un número de punto flotante
    vector = [float(elemento) for elemento in elementos]
   

    #print("Vector toString")
    #print(vector)
    return vector



# Calculate Euclidean distance
# Return Float
def euclidianaDistance(vector1, vector2):
    dist = np.sqrt(np.sum(np.square(vector1 - vector2)))
    return dist


def savePath(f):
    # si queremos guardar la foto
    filename = f.filename
    #path = "C://LaSalle//2022-II//ConstruccionSoftware//Parcial//img//" + filename
    path = "C://Users//Usuario//Desktop//Ejemplo//proyecto_asistencias//Fotos" + filename
    f.save(path)  

    return path


def callOpenFaceAPI(path):
    #url = 'http://127.0.0.1:81/openfaceAPI'
    url = 'http://localhost:81/openfaceAPI'
    #files = {'file': open(path, 'rb')}

    img1 = open('Fotos/joel.jpg', 'rb')
    files = {'imagen1': img1}

    result = requests.post(url, files=files)
    result = result.json()

    return result


# Dictionary to string
# Return list string
def dictToString(dic):
    res = []
    result = dic['result'].replace("\n", "").replace("  ", " ").replace("[", "").replace("]", "") 
    result = list(result.split(' ')) 
    for i in result:
        if i == '':
            pass
        else:
            res.append(i)
    return res

# JSON to String
# Return list string
def toString(string):
    result = string.replace('{','').replace('}','')
    result = list(result.split(','))
    return result

def toFloat(arr):
    vector = []
    for i in arr:
        vector.append(float(i))
    return vector

