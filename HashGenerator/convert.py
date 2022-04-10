import hashlib
import base64
from functions import *


def sha1_convert(string):
    clear()
    result = hashlib.sha1(string.encode('utf-8'))
    print(f'\nSHA1: {result.hexdigest()}')
    print()
    

def sha256_convert(string):
    clear()
    result = hashlib.sha256(string.encode('utf-8'))
    print(f'\nSHA256: {result.hexdigest()}')
    print()


def md5_convert(string):
    clear()
    result = hashlib.md5(string.encode('utf-8'))
    print(f'\nMD5: {result.hexdigest()}')
    print()


def sha512_convert(string):
    clear()
    result = hashlib.sha512(string.encode('utf-8'))
    print(f'\nSHA512: {result.hexdigest()}')
    print()


def base64_convert(string):
    clear()
    result = base64.b64encode(string.encode('utf-8'))
    result_encoded = result.decode('utf-8')
    print(f'\nBase64: {result_encoded}')
    print()