from pycipher import Playfair

plaintext = "abbabba"
key = "abbabba"

cipher = Playfair(key)
encrypted_text = cipher.encipher(plaintext)
print("Encrypted:", encrypted_text)

decrypted_text = cipher.decipher(encrypted_text)
print("Decrypted:", decrypted_text)
