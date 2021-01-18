"""
Szyfrowanie tekstu przy pomocy algorytmu AES.

Autor: Maciej Milewski
Źródło algorytmu szyfrującego: https://pypi.org/project/pycrypto/
"""

from Crypto.Cipher import AES
import base64
from utils import pad, unpad, fill_to_block


def aes_encode(message, key):
    """ Encrypting message using AES in CBC Mode """
    key = bytes(key, encoding='utf8')
    iv = "mm88!@#$%^dsmdms"
    iv = bytes(iv, encoding='utf8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    AES_code = bytes(pad(message), encoding='utf8')
    code = cipher.encrypt(AES_code)
    encrypted_text = str((base64.encodebytes(code)).decode())
    return encrypted_text


def aes_decode(message, key):
    """ Decrypting message and removing padding from message """
    key = bytes(key, encoding='utf8')
    iv = "mm88!@#$%^dsmdms"
    iv = bytes(iv, encoding='utf8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    message = base64.b64decode(message.encode())
    decrypted_text = cipher.decrypt(message).decode()
    decrypted_code = decrypted_text.rstrip('\0')
    return unpad(decrypted_code)