from flask import Flask, request, jsonify
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
from datetime import date

from DBfiles.DBElevi import *
from DBfiles.DBParinti import *
from DBfiles.DBProfi import *
from DBfiles.NewDays import *
from DBfiles.DbConnector import *
from DBfiles.LoghIN import *
from DBfiles.DBLicee import *
from DBfiles.Presence import *
from DBfiles.SendingEmail import *
from DBfiles.AddPresence import *

app = Flask(__name__)
app.config.from_object(__name__)

threads = []
path = 'frontend/src/assets/qrcodes/entrance/qrcode.png'
path_engleza = 'frontend/src/assets/qrcodes/engleza/qrcode.png'
path_informatica = 'frontend/src/assets/qrcodes/informatica/qrcode.png'
path_matematica = 'frontend/src/assets/qrcodes/matematica/qrcode.png'
path_romana = 'frontend/src/assets/qrcodes/romana/qrcode.png'

today = str(date.today())
today = today[5:]
today = today.split('-')
month = str(today[0])
day = str(today[1])
today = day + "." + month
print('Today is: ' + today)

db = mysql.connector.connect(host = 'sql7.freemysqlhosting.net', database = 'sql7588695', user = "sql7588695", passwd = "u3icbbgMbM")

if (db):
    print('Connection to the database is successful')
else:
    print('Connection to the database is unsuccessful')

public_key, private_key = rsa.newkeys(2048)
tempstr = str(public_key).split('(')
tempstr = tempstr[1].split(')')
tempstr = tempstr[0].split(', ')
public_key_string_n = tempstr[0]
public_key_string_e = tempstr[1]
public_key_arr = tempstr
temp_pk = rsa.PublicKey(int(tempstr[0]), int(tempstr[1]))
tempstr = str(private_key).split('(')
tempstr = tempstr[1].split(')')
tempstr = tempstr[0].split(', ')
private_key_arr = tempstr
temp_pk = rsa.PublicKey(int(public_key_arr[0]), int(public_key_arr[1]))
temp_pr = rsa.PrivateKey(int(private_key_arr[0]), int(private_key_arr[1]), int(private_key_arr[2]), int(private_key_arr[3]), int(private_key_arr[4]))

@app.route('/publickey', methods=['GET'])
def publicKey():
    return jsonify(
        public_n = public_key_string_n,
        public_e = public_key_string_e
    )

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
        'name_surname_parinte': data['name_surname_parinte'],
    }
    addChilds(new_parinte['name_surname_copil'], new_parinte['name_surname_parinte'])
    return('Child added')

entrance_qr_string = ''
engleza_qr_string = ''
informatica_qr_string = ''
matematica_qr_string = ''
romana_qr_string = ''

@app.route('/sendentrancestring', methods=['GET'])
def sendEntranceString():
    return(entrance_qr_string)

@app.route('/sendenglezastring', methods=['GET'])
def sendEnglezaString():
    return(engleza_qr_string)

@app.route('/sendinformaticastring', methods=['GET'])
def sendInformaticaString():
    return(informatica_qr_string)

@app.route('/sendmatematicastring', methods=['GET'])
def sendMatematicaString():
    return(matematica_qr_string)

@app.route('/sendromanastring', methods=['GET'])
def sendRomanaString():
    return(romana_qr_string)

@app.route('/entrance', methods=['GET', 'POST'])
def entrance():
    data = request.get_json()
    data_string = str(data['secretkey'])
    data_byte = bytes(data_string, 'ISO-8859-1')
    global temp_pk
    global temp_pr
    decrypted = rsa.decrypt(data_byte, temp_pr).decode()
    decrypted = decrypted.split("/")
    tempstr = decrypted[0] + "/"
    tempstr = tempstr + decrypted[1] + "/"
    tempstr = tempstr + decrypted[2] + "/"
    global entrance_qr_string
    if tempstr == entrance_qr_string:
        idnp = str(decrypted[3])
        global today
        prezent_liceu(idnp, today)
        print("Presence is set")
        return("Presence is set. Have a nice school day!")
    else:
        print("Something went wrong.")
        return('Something went wrong')

@app.route('/engleza', methods=['GET', 'POST'])
def engleza():
    data = request.get_json()
    data_string = str(data['secretkey'])
    data_byte = bytes(data_string, 'ISO-8859-1')
    global temp_pk
    global temp_pr
    decrypted = rsa.decrypt(data_byte, temp_pr).decode()
    decrypted = decrypted.split("/")
    tempstr = decrypted[0] + "/"
    tempstr = tempstr + decrypted[1] + "/"
    tempstr = tempstr + decrypted[2] + "/"
    global engleza_qr_string
    if tempstr == engleza_qr_string:
        idnp = str(decrypted[3])
        global today
        prezent("engleza", idnp, today)
        print("Presence is set")
        return("Presence is set. Have a nice lesson!")
    else:
        print("Something went wrong.")
        return('Something went wrong')
    
@app.route('/informatica', methods=['GET', 'POST'])
def informatica():
    data = request.get_json()
    data_string = str(data['secretkey'])
    data_byte = bytes(data_string, 'ISO-8859-1')
    global temp_pk
    global temp_pr
    decrypted = rsa.decrypt(data_byte, temp_pr).decode()
    decrypted = decrypted.split("/")
    tempstr = decrypted[0] + "/"
    tempstr = tempstr + decrypted[1] + "/"
    tempstr = tempstr + decrypted[2] + "/"
    global informatica_qr_string
    if tempstr == informatica_qr_string:
        idnp = str(decrypted[3])
        global today
        prezent("informatica", idnp, today)
        print("Presence is set")
        return("Presence is set. Have a nice lesson!")
    else:
        print("Something went wrong.")
        return('Something went wrong')
    
@app.route('/matematica', methods=['GET', 'POST'])
def matematica():
    data = request.get_json()
    data_string = str(data['secretkey'])
    data_byte = bytes(data_string, 'ISO-8859-1')
    global temp_pk
    global temp_pr
    decrypted = rsa.decrypt(data_byte, temp_pr).decode()
    decrypted = decrypted.split("/")
    tempstr = decrypted[0] + "/"
    tempstr = tempstr + decrypted[1] + "/"
    tempstr = tempstr + decrypted[2] + "/"
    global matematica_qr_string
    if tempstr == matematica_qr_string:
        idnp = str(decrypted[3])
        global today
        prezent("matematica", idnp, today)
        print("Presence is set")
        return("Presence is set. Have a nice lesson!")
    else:
        print("Something went wrong.")
        return('Something went wrong')
    
@app.route('/romana', methods=['GET', 'POST'])
def romana():
    data = request.get_json()
    data_string = str(data['secretkey'])
    data_byte = bytes(data_string, 'ISO-8859-1')
    global temp_pk
    global temp_pr
    decrypted = rsa.decrypt(data_byte, temp_pr).decode()
    decrypted = decrypted.split("/")
    tempstr = decrypted[0] + "/"
    tempstr = tempstr + decrypted[1] + "/"
    tempstr = tempstr + decrypted[2] + "/"
    global romana_qr_string
    if tempstr == romana_qr_string:
        idnp = str(decrypted[3])
        global today
        prezent("romana", idnp, today)
        print("Presence is set")
        return("Presence is set. Have a nice lesson!")
    else:
        print("Something went wrong.")
        return('Something went wrong')

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

def generate_qr(sc):
    global entrance_qr_string
    place = "entrance"
    time = today
    rand_string = get_random_string(8)
    qr_string = place + "/" + time + "/" + rand_string + "/"
    entrance_qr_string = qr_string
    img = qrcode.make(qr_string)
    img.save(path)
    
    global engleza_qr_string
    place = "engleza"
    time = today
    rand_string = get_random_string(8)
    qr_string = place + "/" + time + "/" + rand_string + "/"
    engleza_qr_string = qr_string
    img = qrcode.make(qr_string)
    img.save(path_engleza)
    
    global informatica_qr_string
    place = "informatica"
    time = today
    rand_string = get_random_string(8)
    qr_string = place + "/" + time + "/" + rand_string + "/"
    informatica_qr_string = qr_string
    img = qrcode.make(qr_string)
    img.save(path_informatica)
    
    global matematica_qr_string
    place = "matematica"
    time = today
    rand_string = get_random_string(8)
    qr_string = place + "/" + time + "/" + rand_string + "/"
    matematica_qr_string = qr_string
    img = qrcode.make(qr_string)
    img.save(path_matematica)
    
    global romana_qr_string
    place = "romana"
    time = today
    rand_string = get_random_string(8)
    qr_string = place + "/" + time + "/" + rand_string + "/"
    romana_qr_string = qr_string
    img = qrcode.make(qr_string)
    img.save(path_romana)
    sc.enter(15, 1, generate_qr, (sc,))

s.enter(1, 1, generate_qr, (s,))

def run_qr_generator():
    s.run()

def run_school():
    school_thread = Thread(target = lambda: app.run(host = '0.0.0.0', port = 5000, debug = True, use_reloader = False), daemon = True)
    threads.append(school_thread)
    qr_delete_thread = Thread(target = delete_old_entrance_qr)
    threads.append(qr_delete_thread)
    qr_thread = Thread(target = run_qr_generator)
    threads.append(qr_thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    run_school()