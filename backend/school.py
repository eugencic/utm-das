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
import datetime
import sys
import codecs


app = Flask(__name__)
app.config.from_object(__name__)


CORS(app, resources={r"/*":{'origins':"*"}})
CORS(app, resources={r'/*':{'origins': 'http://localhost:8080', "allow_headers": "Access-Control-Allow-Origin"}})


threads = []
path = 'frontend/src/assets/qrcodes/entrance/qrcode.png'


# with open('backend/keys/publicKey.pem', 'rb') as p:
#     public_key = rsa.PublicKey.load_pkcs1(p.read())
# with open('backend/keys/privateKey.pem', 'rb') as p:
#     private_key = rsa.PrivateKey.load_pkcs1(p.read())
# with open('backend/keys/publicKey.pem', 'rb') as p:
#     original_public_key = str(p.read())

key_pair = RSA.generate(2048)

public_key = key_pair.publickey().exportKey()
private_key = key_pair.exportKey()

print(public_key)
print(type(public_key))
print(private_key)
    
    
@app.route('/publickey', methods=['GET'])
def publicKey():
    return(public_key)


entrance_qr_string = ''

@app.route('/sendentrancestring', methods=['GET'])
def sendEntranceString():
    return(entrance_qr_string)


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
    

db = mysql.connector.connect(host = 'sql7.freemysqlhosting.net', database = 'sql7588695', user = "sql7588695", passwd = "u3icbbgMbM")

if (db):
    print('Connection successful')
else:
    print('Connection unsuccessful')
    
mycursor = db.cursor()


def delete_old_entrance_qr():
    if os.path.exists(path):
        im = Image.open('frontend/src/assets/qrcodes/entrance/empty_qrcode.png')
        im.save(path)


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


s = sched.scheduler(time.time, time.sleep)

def generate_entrance_qr(sc):
    global entrance_qr_string
    place = "entrance"
    time = str(datetime.datetime.now())
    rand_string = get_random_string(8)
    qr_string = place + "/" + time + "/" + rand_string
    entrance_qr_string = qr_string
    img = qrcode.make(qr_string)
    img.save(path)
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