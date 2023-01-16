from flask import Flask, request
import requests
import rsa
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import sys


app = Flask(__name__)
app.config.from_object(__name__)

p_key = requests.get("http://127.0.0.1:5000/publickey")
p_key = p_key.text
p_key = RSA.importKey(p_key)
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

cipher = PKCS1_OAEP.new(p_key)
encrypted_message = cipher.encrypt(data_string.encode())
print(encrypted_message)
print(sys.getsizeof(encrypted_message))

# encrypted_message = rsa.encrypt(data_string.encode(), public_key)
# print(encrypted_message)
encrypted_message = str(encrypted_message)
encrypted_message = encrypted_message[2:-1]
print(encrypted_message)
print(sys.getsizeof(encrypted_message))
#encrypted_message = encrypted_message.encode()
#decrypted = rsa.decrypt(encrypted_message, private_key).decode()

myobj = {'secretkey': encrypted_message}

x = requests.post("http://127.0.0.1:5000/entrance", json = myobj)

if __name__ == '__main__':
    app.run(debug=True, port=8001)