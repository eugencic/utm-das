from flask import Flask, request
import requests
import rsa
# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP
import sys
import json


app = Flask(__name__)
app.config.from_object(__name__)


p_key = requests.get("http://127.0.0.1:5000/publickey")
p_key_map = p_key.json()
# p_key_map = json.load(p_key_json)
p_key_n = p_key_map['public_n']
p_key_e = p_key_map['public_e']
p_key = rsa.PublicKey(int(p_key_n),int(p_key_e))
print(p_key)

qr_message = requests.get("http://127.0.0.1:5000/sendentrancestring")
qr_message = str(qr_message.text)
print(qr_message)


# with open('keys/publicKey.pem', 'rb') as p:
#     public_key = rsa.PublicKey.load_pkcs1(p.read())
# with open('keys/privateKey.pem', 'rb') as p:
#     private_key = rsa.PrivateKey.load_pkcs1(p.read())

idnp = str("0123456789")

data_string = qr_message + idnp

encrypted_message = rsa.encrypt(data_string.encode(), p_key)
print(encrypted_message)
# print(sys.getsizeof(encrypted_message))

# encrypted_message = rsa.encrypt(data_string.encode(), public_key)
# print(encrypted_message)
encrypted_message_string = str(encrypted_message, 'ISO-8859-1')
# encrypted_message = encrypted_message[2:-1]
# print(encrypted_message)
# print(sys.getsizeof(encrypted_message))
#encrypted_message = encrypted_message.encode()
#decrypted = rsa.decrypt(encrypted_message, private_key).decode()

myobj = {'secretkey': encrypted_message_string}

x = requests.post("http://127.0.0.1:5000/receiveqr", json = myobj)

if __name__ == '__main__':
    app.run(debug=True, port=8001)