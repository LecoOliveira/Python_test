#!/usr/bin/python3
# Coded by: Alex Rocha
# Contact: lecoverde10@gmail.com
#
# Usage: Python3 hash_generator.py
#

from functions import *
from option import choose_conversion


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

        
    
