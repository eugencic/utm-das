import rsa

publicKey, privateKey = rsa.newkeys(2048)

# this is the string that we will be encrypting
message = "hello geeks"
tempstr = str(publicKey).split('(')
tempstr = tempstr[1].split(')')
tempstr = tempstr[0].split(', ')
print(tempstr)
tempPK = rsa.PublicKey(int(tempstr[0]), int(tempstr[1]))
print(str(publicKey))
print(type(publicKey))

encMessage = rsa.encrypt(message.encode(),
                         tempPK)
encMessage_string = str(encMessage, 'ISO-8859-1')


print("original string: ", message)
print("encrypted string: ", encMessage)
print("encrypted string: ", encMessage_string)
data_byte = bytes(encMessage_string,'ISO-8859-1')

decMessage = rsa.decrypt(data_byte, privateKey).decode()

print("decrypted string: ", decMessage)