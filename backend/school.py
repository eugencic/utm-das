from flask import Flask
from flask_cors import CORS
from threading import Thread
from PIL import Image
import sched
import time
import os
import string
import random
import qrcode

app = Flask(__name__)
app.config.from_object(__name__)


CORS(app, resources={r"/*":{'origins':"*"}})
CORS(app, resources={r'/*':{'origins': 'http://localhost:8080', "allow_headers": "Access-Control-Allow-Origin"}})


threads = []
path = 'frontend/src/assets/qrcodes/entrance/qrcode.png'


@app.route('/entrance', methods=['GET'])
def entrance():
    return("Scan the QR Code when you enter and leave the school")


def delete_old_qr():
    if os.path.exists(path):
        im = Image.open('frontend/src/assets/qrcodes/entrance/empty_qrcode.png')
        im.save(path)

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


s = sched.scheduler(time.time, time.sleep)

def generate_qr(sc):
    rand_string = get_random_string(8)
    img = qrcode.make(rand_string)
    img.save(path)
    sc.enter(15, 1, generate_qr, (sc,))

s.enter(1, 1, generate_qr, (s,))


def run_qr_generator():
    s.run()


def run_school():
    school_thread = Thread(target = lambda: app.run(host = '0.0.0.0', port = 5000, debug = True, use_reloader = False), daemon = True)
    threads.append(school_thread)
    qr_delete_thread = Thread(target = delete_old_qr)
    threads.append(qr_delete_thread)
    qr_thread = Thread(target = run_qr_generator)
    threads.append(qr_thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    run_school()