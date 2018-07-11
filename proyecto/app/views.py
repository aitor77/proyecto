import datetime
import json

import requests
from flask import render_template, redirect, request
from flaskext.mysql import MySQL

from Crypto.Cipher import PKCS1_v1_5, AES
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import  RSA
from datetime import time

from app import app
from arbol_merkel import  *

# The node with which our application interacts, there can be multiple
# such nodes as well.
CONNECTED_NODE_ADDRESS = "http://127.0.0.1:8000"



mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'blockchain'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()
indice = 0
start_time = time(0,0,0)
end_time = time (0,30,0)
posts = []
LISTA = []
aux = []

while start_time:
    manda_bloque()
    if end_time:
        break

def manda_bloque():

    indice = (indice +1)
    mi_arbol = ArbolMerkel()
    aux.append(LISTA)
    LISTA = []
    mi_arbol.lista = aux
    mi_arbol.crear_arbol()
    diccionario = mi_arbol.get_diccionario()

    insertCmd = "insert into temporal (id, archivo, dia) values ('" + indice + "','" + json.dumps(diccionario, ident=4) + "','"+ datetime.datetime.now()+"';"
    try:
        cursor.execute(insertCmd)
        conn.commit()
        print("arrbols guardado en la base")
    except Exception as e:
        print("Hubo un problema al insertar los datos:" + str(e))

    post_object = {
        'dia' : datetime.date.now(),
        'content': mi_arbol.get_raiz(),
    }

    # Submit a transaction
    new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})

    result = redirect( "{{node_address}}/mine")

    if result == 0:
        print ("El nodo no entro en la cadena de bloques")
    else:
        insertCmd = "insert into registro (idregistro, fecha, arbolmerkel, listaArbol, json) values ('" + indice + "','" + datetime.datetime.now() + "','" + mi_arbol.get_raiz() + "','"+aux+"','"+ json.dumps(diccionario,
                                                                                                      ident=4) +"';"
        try:
            cursor.execute(insertCmd)
            conn.commit()
            print("El nodo ha entrado en la cadena de bloques correctamente")
            aux = []
        except Exception as e:
            print("Hubo un problema al insertar los datos:" + str(e))






def fetch_posts():

    get_chain_address = "{}/chain".format(CONNECTED_NODE_ADDRESS)
    response = requests.get(get_chain_address)
    if response.status_code == 200:
        content = []
        chain = json.loads(response.content)
        for block in chain["chain"]:
            for tx in block["transactions"]:
                tx["index"] = block["index"]
                tx["hash"] = block["previous_hash"]
                content.append(tx)

        global posts
        posts = sorted(content, key=lambda k: k['timestamp'],
                       reverse=True)


@app.route('/')
def index():
    fetch_posts()
    return render_template('index.html',
                           title='Inicio',
                           posts=posts,
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string)


@app.route('/submit', methods=['POST'])
def submit_text():
    name = request.form["author"]
    key = request.form["key"]

    if key and name:
        insertCmd = "insert into usuarios (nombre, publicKey) values ('"+name+"','"+key+"');"
        try:
            cursor.execute(insertCmd)
            conn.commit()
            return json.dumps({'message':'Usuario registrado correctamente'})
        except Exception as e:
            print("Hubo un problema al insertar los datos:" + str(e))
            return json.dumps({'error': 'Hubo un error al intentar ingresar los datos'})
    else:
        return json.dumps({'error':'Tienen que rellenarse todos los campos'})


@app.route('/envios')
def envios():
    fetch_posts()
    return render_template('envios.html',
                           title='Envios',
                           posts=posts,
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string)

@app.route('/submitB', methods=['POST'])
def submit_archivo():
    name = request.form["author"]
    file = request.form["archivo"]
    save = request.form.get('guardar')
    encrip = request.form.get('encriptar')
    if name and file:
        selectCmd = "select publicKey from usuarios where (nombre='"+name+"');"
        insertCmd = "insert into datos (nombre, archivo) values ('"+name+"','"+file+"');"
        if save and encrip:
            cursor.execute(selectCmd)
            key = cursor.fetchone()
            try:
                cursor.execute(insertCmd)
                conn.commit()
            except Exception as e:
                print("Hubo un problema al insertar los datos:" + str(e))
                return json.dumps({'error': 'Hubo un error al intentar ingresar los datos'})
            b = encriptar(key,file)
            LISTA.append(b)

            return json.dumps({'message': 'guardar y encriptar'})

        elif save:
            try:
                cursor.execute(insertCmd)
                conn.commit()
            except Exception as e:
                print("Hubo un problema al insertar los datos:" + str(e))
                return json.dumps({'error': 'Hubo un error al intentar ingresar los datos'})
            LISTA.append(file)
            return json.dumps({'message':'guardar'})

        elif encrip:
            cursor.execute(selectCmd)
            key = cursor.fetchone()
            b = encriptar(key,file)
            LISTA.append(b)
            return json.dumps({'message': 'encriptar'})

        else:
            LISTA.append(file)
            return json.dumps({'message': 'ni guardar ni encriptar'})
    else:
        return json.dumps({'error': 'Tienen que rellenarse todos los campos'})


def encriptar(clave,archivo):
    if clave == None:
        print("El usuario no tiene clave publica asignada")
    else:

        # Cargamos la clave publica
        key = RSA.importKey(clave)
        # Instancia del cifrador asimetrico
        cipher_rsa = PKCS1_v1_5.new(key)
        # Generamos una clave para el cifrado simetrico
        aes_key = get_random_bytes(16)
        # Encriptamos la clave simetrico con la clave publica RSA
        enc_aes_key = cipher_rsa.encrypt(aes_key)

        # Abro el fichero lo copio en memoria y lo cierro
        f = open(archivo, 'rb+')
        d = f.read()
        f.close()

        # Encriptamos los datos con la clve simetrica
        cipher_aes = AES.new(aes_key, AES.MODE_EAX)
        d = cipher_aes.encrypt(d, ' ')
        f = open(archivo, 'wb+')
        f.write(d)
        # Aniadimos la clave simetrica codificada en la ultima linea del archivo
        f.write("\n")
        f.write(enc_aes_key)
        f.close()

        return f

def timestamp_to_string(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%H:%M')


