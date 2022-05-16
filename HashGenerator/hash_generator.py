#!/usr/bin/python3
# Coded by: Alex Rocha
# Contact: lecoverde10@gmail.com
#
# Usage: Python3 hash_generator.py
#

from convert import *
from functions import *

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


def main():

    try:
        clear()
        while True:
            string = input('Type the text to be encoded: ')
            title()
            choose_conversion(string)
            if not cont():
                break        


    except ValueError:
        print('\nInvalid character. Type a number between 1 and 6.')
    except Exception as error:
        print(f'\nError: {str(error)}')
    except KeyboardInterrupt:
        sleep(0.5)
        print('\n\nEnd program!')

main()

        
    
