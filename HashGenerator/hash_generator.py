#!/usr/bin/python3
# Coded by: Alex Rocha
# Contact: lecoverde10@gmail.com
#
# Usage: Python3 hash_generator.py
#

from convert import *
from functions import *


try:

    clear()
    while True:
        string = input('Type the text to be encoded: ')
        title()
        options = int(input('\nSelect the option: '))
        
        time.sleep(1)
        while options < 1 or options > 6:
            print('\nInvalid option')
            options = int(input('Type a number between 1 and 6: '))

        if options == 1:
            sha1_convert(string)
            if cont():
                continue
            else:
                break           

        elif options == 2:
            sha256_convert(string)
            if cont():
                continue
            else:
                break

        elif options == 3:
            md5_convert(string)
            if cont():
                continue
            else:
                break

        elif options == 4:
            sha512_convert(string)
            if cont():
                continue
            else:
                break

        elif options == 5:
            base64_convert(string)
            if cont():
                continue
            else:
                break

        elif options == 6:
            print('End program.')
            time.sleep(1)
            clear()
            break

except ValueError:
    print('\nInvalid character. Type a number between 1 and 6.')
except Exception as error:
    print(f'\nError: {str(error)}')
except KeyboardInterrupt:
    time.sleep(0.5)
    print('\n\nEnd program!')
        
    
