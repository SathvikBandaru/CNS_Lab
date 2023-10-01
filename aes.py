# pip install pycryptodome 
#importing AES
from Crypto.Cipher import AES

key = b'C&F)H@McQfTjWnZr'
cipher = AES.new(key, AES.MODE_EAX)
data = "Welcome to copyassignment.com!".encode()
nonce = cipher.nonce
ciphertext = cipher.encrypt(data)
print("Plain text:", data)

print("Cipher text:", ciphertext)
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
dectext = cipher.decrypt(ciphertext)
print("Decrypted text:", dectext)
