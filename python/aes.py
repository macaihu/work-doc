
import sys
from Crypto.Cipher import AES
def encode():
  obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
  org_fiile = open('../others/pass.txt', 'r')
  message = org_fiile.read()
  length = 16 - (len(message) % 16)
  message += chr(length)*length
  ciphertext = obj.encrypt(message)
  #print ciphertext
  ace_file = open('../others/pass', 'w')
  ace_file.write(ciphertext)

def decode():
  obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
  ace_file = open('../others/pass', 'r')
  message = ace_file.read()
  orgtext = obj2.decrypt(message)
  print orgtext  


if __name__ == '__main__':
	if sys.argv[1] == 'encode':
		encode()
	elif sys.argv[1] == "decode":
		decode()
