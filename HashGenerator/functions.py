import os
import time


def clear():

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def title():
    print('''\n========================================
=========== CHOOSE HASH TYPE ===========
  [1] SHA1     [3] MD5      [5] Base64
  [2] SHA256   [4] SHA512   [6] Exit
========================================''')

def cont():
    key = True
    repeat = input('Do you want to encript another text (y/n)? ').lower()
    if repeat == 'y':
        clear()
        return key
    elif repeat == 'n':
        print()
        time.sleep(0.5)
        print('End Program.')
        key = False
    else:
        clear()
        print('INVALID OPTION')
        print('(Type y or n)\n')
        return cont()

