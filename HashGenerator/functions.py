from os import system, name
from time import sleep
from convert import *


def clear():

    if name == 'nt':
        system('cls')
    else:
        system('clear')


def title():
    
    print(
        f'\n{"":=>40}'
        f'\n{" CHOOSE HASH TYPE ":=^40}',
        f'\n{"[1] SHA1":^12}', f'{"[2] SHA256":^13}',
        f'{"[3] SHA512":^12}', f'\n{"[4] MD5":^12}',
        f'{"[5] Base64":^12}', f'{"[6] SAIR":^12}',
        f'\n{"":=^40}\n'
    )


def cont():
    key = True
    repeat = input('Do you want to encript another text (y/n)? ').lower()
    
    if repeat == 'y':
        clear()
        return key 

    elif repeat == 'n':
        sleep(0.5)
        print('\nEnd Program.')
        key = False
    
    else:
        clear()
        print(
            'INVALID OPTION',
            '\n(Type y or n)\n'
        )
        
        return cont()
        

def choose_conversion(string):

    options = int(input('Select the option: '))
    sleep(1)

    while options < 1 or options > 6:
        print('\nInvalid option')
        options = int(input('Type a number between 1 and 6: '))
    
    if options == 6:
        print('End program.')
        sleep(1)
        clear()
        return exit()

    convert = {
        1: lambda string: sha1_convert(string),
        2: lambda string: sha256_convert(string),
        3: lambda string: sha512_convert(string),
        4: lambda string: md5_convert(string),
        5: lambda string: base64_convert(string)
    }
    return convert[options](string)

