import crypto
import sys
sys.modules['Crypto'] = crypto
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import hashlib
BLOCK_SIZE = 256

# This function encrypt plaintext with AES algorithm
def AES_Encrypt(plaintext, key):
	AESkey = key
	cipher = AES.new(AESkey, AES.MODE_ECB)
	ciphertext = cipher.encrypt(pad(plaintext.encode(), BLOCK_SIZE))
	return ciphertext


# This function decrypt ciphertext with key
def AES_Decrypt(ciphertext, key):
	cipherfordecrypt = AES.new(key, AES.MODE_ECB)
	plaintext = unpad(cipherfordecrypt.decrypt(ciphertext), BLOCK_SIZE)
	return plaintext


# This function makes hashvalue with SHA256
def SHA_Hash(plaintext):
	hashvalue = hashlib.sha256(plaintext.encode()).hexdigest()
	return hashvalue


#This function encrypt plaintext with RSA algorithm
def RSA_Encrypt(plaintext):
	#RSA key pair generator, length is 2048 bit	
	private_key = RSA.generate(2048)
	public_key = private_key.publickey()
	cipher_rsa = PKCS1_OAEP.new(public_key)
	ciphertext = cipher_rsa.encrypt(temp_plain_text.encode())
	return ciphertext, private_key


#This function decrypt ciphertext with RSA decryption
def RSA_Decrypt(ciphertext, private_key):
	cipher_rsa = PKCS1_OAEP.new(private_key)
	plaintext = cipher_rsa.decrypt(ciphertext)
	return plaintext


if __name__ == '__main__':	
	# Input plaintext
	print("original data:")
	temp_plain_text = input()
	print()

	# AES Encryption and Decryption
	print("cipher type(AES): AES")
	print("key(16/24/32):")
	# Accept key for AES
	temp_key = input().encode()
	# Encryption with AES
	ciphertext = AES_Encrypt(temp_plain_text, temp_key)
	# Decryption with AES
	plaintext = AES_Decrypt(ciphertext, temp_key)
	print("encrypted: ", ciphertext)
	print("decrypted: ", plaintext.decode(), "\n")

	# SHA 256 hash function	
	print("hash type(SHA256): SHA256")
	hashvalue = SHA_Hash(temp_plain_text)
	print(hashvalue, "\n")

	# RSA Encryption and Decryption
	print("RSA")
	print("key length(x256, >=1024): 2048")
	# Encryption with RSA
	ciphertext, private_key = RSA_Encrypt(temp_plain_text.encode())
	print("encrypted: ", ciphertext)
	# Decryption with RSA
	plaintext = RSA_Decrypt(ciphertext, private_key)
	print("decrypted: ", plaintext.decode("utf-8"))
