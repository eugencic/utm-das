from flask import Flask, request
import requests
import rsa
import sys
import json


app = Flask(__name__)
app.config.from_object(__name__)

p_key = requests.get("http://127.0.0.1:5000/publickey")
p_key_map = p_key.json()
p_key_n = p_key_map['public_n']
p_key_e = p_key_map['public_e']
p_key = rsa.PublicKey(int(p_key_n),int(p_key_e))
print(p_key)

qr_message = requests.get("http://127.0.0.1:5000/sendentrancestring")
qr_message = str(qr_message.text)
print(qr_message)

test_idnp = str("0123456789")

data_string = qr_message + '/' + test_idnp

encrypted_message = rsa.encrypt(data_string.encode(), p_key)
print(encrypted_message)

encrypted_message_string = str(encrypted_message, 'ISO-8859-1')

myobj = {'secretkey': encrypted_message_string}

x = requests.post("http://127.0.0.1:5000/entrance", json = myobj)

if __name__ == '__main__':
    app.run(debug=True, port=8001)