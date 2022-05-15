import os
import time


def clear():

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


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
        print()
        time.sleep(0.5)
        print('End Program.')
        key = False
    else:
        clear()
        print('INVALID OPTION')
        print('(Type y or n)\n')
        return cont()

