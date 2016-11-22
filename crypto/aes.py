__author__ = 'ruiqin'

from Crypto.Cipher import AES
from base64 import b64decode

def aes_dec(cipher, key):
    obj = AES.new(key, AES.MODE_CBC, '\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0')
    return obj.decrypt(b64decode(cipher))
