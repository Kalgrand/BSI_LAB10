"""
Szyfrowanie tekstu przy pomocy algorytmu AES.

Autor: Maciej Milewski
Źródło algorytmu szyfrującego: https://pypi.org/project/pycrypto/
"""

from Crypto.Cipher import AES
import base64
from utils import pad, unpad, fill_to_block


# def pad(s):
#     """ Adds padding for message before encryption """
#     pad = 16 - len(s) % 16
#     return s + pad * chr(pad)

# def unpad(s):
#     """ Removes padding after decryption """
#     offset = ord(s[-1])
#     return s[:-offset]

# def fill_to_block(message, size):
#     """ Adds whitespaces to message """
#     reminder = len(message)%size
#     if(reminder == 0):
#         return message
#     else:
#         for i in range(0, size-reminder):
#             message += " "
#         return message


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


""" Crypt&Decrypt message using AES """
# message = input("Podaj wiadomość: \n")
# secret_key = input("Podaj klucz (musi być 16 znaków!): \n")
# secret_key = fill_to_block(secret_key, 16)

# encrypted_text = aes_encode(message, secret_key)

# decrypted_text = aes_decode(encrypted_text, secret_key)

# print('Zaszyfrowany tekst: ', encrypted_text)
# print('Odszyfrowany tekst: ', decrypted_text)

