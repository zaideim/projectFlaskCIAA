from flask import Flask, render_template,jsonify,request
import numpy as np
from joblib import load
import os

#Cargar el modelo
dt=load('dt1.jpblib')

#Servidor(Backend)
servidorWeb = Flask(__name__)
@servidorWeb.route("/holamundo",methods = ['GET'])
def formulario():
    return render_template('pagina1.html')

#    return render_template('pagina1.html')

#Envio de datos a través de JSON
@servidorWeb.route('/modelo',methods=['POST'])
def modeloPrediccion():
    contenido = request.json
    print(contenido)
    return jsonify({'resultado':"Hola"})

if __name__ == '__main__':
   servidorWeb.run(debug=False, host = '0.0.0.0', port ='8080')
