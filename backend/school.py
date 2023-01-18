from flask import Flask, request
from flask_cors import CORS
from threading import Thread
from PIL import Image
import sched
import time
import os
import string
import random
import qrcode
import mysql.connector
import rsa
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from datetime import date
import sys
import codecs

from DBfiles.DBElevi import *
from DBfiles.DBParinti import *
from DBfiles.DBProfi import *
from DBfiles.LoghIN import *


app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})
CORS(app, resources={r'/*':{'origins': 'http://localhost:8080', "allow_headers": "Access-Control-Allow-Origin"}})

threads = []
path = 'frontend/src/assets/qrcodes/entrance/qrcode.png'
path_engleza = 'frontend/src/assets/qrcodes/engleza/qrcode.png'
path_informatica = 'frontend/src/assets/qrcodes/informatica/qrcode.png'
path_matematica = 'frontend/src/assets/qrcodes/matematica/qrcode.png'
path_romana = 'frontend/src/assets/qrcodes/romana/qrcode.png'

today = str(date.today())
today = today[5:]
today = today.replace("-", ".")
print(today)

db = mysql.connector.connect(host = 'sql7.freemysqlhosting.net', database = 'sql7588695', user = "sql7588695", passwd = "u3icbbgMbM")

if (db):
    print('Connection successful')
else:
    print('Connection unsuccessful')
    
mycursor = db.cursor()

# with open('backend/keys/publicKey.pem', 'rb') as p:
#     public_key = rsa.PublicKey.load_pkcs1(p.read())
# with open('backend/keys/privateKey.pem', 'rb') as p:
#     private_key = rsa.PrivateKey.load_pkcs1(p.read())
# with open('backend/keys/publicKey.pem', 'rb') as p:
#     original_public_key = str(p.read())

# key_pair = RSA.generate(2048)

# public_key = key_pair.publickey().exportKey()
# private_key = key_pair.exportKey()

# print(public_key)
# print(type(public_key))
# print(private_key)
     
# @app.route('/publickey', methods=['GET'])
# def publicKey():
#     return(public_key)

entrance_qr_string = ''
engleza_qr_string = ''
informatica_qr_string = ''
matematica_qr_string = ''
romana_qr_string = ''

@app.route('/sendentrancestring', methods=['GET'])
def sendEntranceString():
    return(entrance_qr_string)

@app.route('/login', methods=['GET', 'POST'])
def login():
    data = request.get_json()
    user = {
        'username': data['username'],
        'password': data['password']
    }
    user_data = signIn(user['username'], user['password'])
    return(str(user_data))

@app.route('/signupelev', methods=['GET', 'POST'])
def signupelev():
    data = request.get_json()
    new_elev = {
        'username': data['username'],
        'password': data['password'],
        'idnp': data['idnp'],
        'name_surname': data['name_surname'],
        'clasa': data['clasa'],
        'liceu': data['liceu'],
        'parinte': data['parinte']
    }
    newuserelev(new_elev['username'], new_elev['password'])
    newelev(new_elev['idnp'], new_elev['name_surname'], new_elev['clasa'], new_elev['liceu'], new_elev['parinte'], new_elev['username'])
    return('User created')

@app.route('/signupparinte', methods=['GET', 'POST'])
def signupparinte():
    data = request.get_json()
    new_parinte = {
        'username': data['username'],
        'password': data['password'],
        'idnp': data['idnp'],
        'name_surname': data['name_surname'],
        'liceu': data['liceu'],
        'posta': data['posta']
    }
    newuserparinte(new_parinte['username'], new_parinte['password'])
    newparinte(new_parinte['idnp'], new_parinte['name_surname'], new_parinte['liceu'], new_parinte['username'], new_parinte['posta'])
    return('User created')

@app.route('/signupprof', methods=['GET', 'POST'])
def signuprof():
    data = request.get_json()
    new_prof = {
        'username': data['username'],
        'password': data['password'],
        'name_surname': data['name_surname'],
        'obiect': data['obiect']
    }
    newuserprof(new_prof['username'], new_prof['password'])
    newprof(new_prof['name_surname'], new_prof['obiect'], new_prof['username'])
    return('User created')

@app.route('/addchildsparinte', methods=['GET', 'POST'])
def addChildsParinte():
    data = request.get_json()
    new_parinte = {
        'name_surname_copil': data['name_surname_copil'],
        'name__surname_parinte': data['name_surname_parinte'],
    }
    addChilds(new_parinte['name_surname_copil'], new_parinte['name_surname_parinte'])
    return('Child added')

@app.route('/entrance', methods=['GET', 'POST'])
def entrance():
    data = request.get_json()
    print(data['secretkey'])
    data_string = str(data['secretkey'])
    data_string = data_string.encode()
    print(sys.getsizeof(data_string))
    print(data_string)
    global private_key
    pr_key = RSA.importKey(private_key)
    cipher = PKCS1_OAEP.new(pr_key)
    decrypted = cipher.decrypt(data_string)
    print(decrypted)
    return {'success': True}
    
def delete_old_entrance_qr():
    if os.path.exists(path):
        im = Image.open('frontend/src/assets/qrcodes/entrance/empty_qrcode.png')
        im.save(path)
              
def delete_old_engleza_qr():
    if os.path.exists(path):
        im = Image.open('frontend/src/assets/qrcodes/engleza/empty_qrcode.png')
        im.save(path)
              
def delete_old_informatica_qr():
    if os.path.exists(path):
        im = Image.open('frontend/src/assets/qrcodes/informatica/empty_qrcode.png')
        im.save(path)

def delete_old_matematica_qr():
    if os.path.exists(path):
        im = Image.open('frontend/src/assets/qrcodes/matematica/empty_qrcode.png')
        im.save(path)
              
def delete_old_romana_qr():
    if os.path.exists(path):
        im = Image.open('frontend/src/assets/qrcodes/romana/empty_qrcode.png')
        im.save(path)

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

s = sched.scheduler(time.time, time.sleep)

def generate_entrance_qr(sc):
    global entrance_qr_string
    place = "entrance"
    time = today
    rand_string = get_random_string(8)
    qr_string = place + "/" + time + "/" + rand_string
    entrance_qr_string = qr_string
    img = qrcode.make(qr_string)
    img.save(path)
    
    global engleza_qr_string
    place = "engleza"
    time = today
    rand_string = get_random_string(8)
    qr_string = place + "/" + time + "/" + rand_string
    engleza_qr_string = qr_string
    img = qrcode.make(qr_string)
    img.save(path_engleza)
    
    global informatica_qr_string
    place = "informatica"
    time = today
    rand_string = get_random_string(8)
    qr_string = place + "/" + time + "/" + rand_string
    informatica_qr_string = qr_string
    img = qrcode.make(qr_string)
    img.save(path_informatica)
    
    global matematica_qr_string
    place = "matematica"
    time = today
    rand_string = get_random_string(8)
    qr_string = place + "/" + time + "/" + rand_string
    matematica_qr_string = qr_string
    img = qrcode.make(qr_string)
    img.save(path_matematica)
    
    global romana_qr_string
    place = "romana"
    time = today
    rand_string = get_random_string(8)
    qr_string = place + "/" + time + "/" + rand_string
    romana_qr_string = qr_string
    img = qrcode.make(qr_string)
    img.save(path_romana)
    sc.enter(15, 1, generate_entrance_qr, (sc,))

s.enter(1, 1, generate_entrance_qr, (s,))

def run_entrance_qr_generator():
    s.run()

def run_school():
    school_thread = Thread(target = lambda: app.run(host = '0.0.0.0', port = 5000, debug = True, use_reloader = False), daemon = True)
    threads.append(school_thread)
    qr_delete_thread = Thread(target = delete_old_entrance_qr)
    threads.append(qr_delete_thread)
    qr_thread = Thread(target = run_entrance_qr_generator)
    threads.append(qr_thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    run_school()