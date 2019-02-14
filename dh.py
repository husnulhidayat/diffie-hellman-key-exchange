import hashlib
import configparser
import random

config = configparser.RawConfigParser()
config.read('agreement.txt')

prime = config.getint('agreement','prime')
p_root = config.getint('agreement','primitiveroot')
spub = config.getint('pubkey','sender')
rpub = config.getint('pubkey','recipient')

prime = prime
root  = p_root

sender_pub = spub
recepient_pub = rpub

sender_calculate = (root**sender_pub) % prime
recepient_calculate = (root**recepient_pub) % prime

print("prime = ",prime,"| primitive root = ",root)

keySender = (recepient_calculate**sender_pub) % prime
keyRecepient = (sender_calculate**recepient_pub) % prime

keySenderSTR = str(keySender)
keyRecepientSTR = str(keyRecepient)

m = hashlib.sha256()
m.update(keySenderSTR.encode('utf-8'))
hexSender = m.hexdigest()

n = hashlib.sha256()
n.update(keyRecepientSTR.encode('utf-8'))
hexRecipient = n.hexdigest()

print("Sender Secret Key    : ",hexSender[:32])
print("Recepient Secret Key : ",hexRecipient[:32])
