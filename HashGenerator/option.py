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
        1: lambda string: print(sha1_convert(string)),
        2: lambda string: print(sha256_convert(string)),
        3: lambda string: print(sha512_convert(string)),
        4: lambda string: print(md5_convert(string)),
        5: lambda string: print(base64_convert(string))
    }
    return convert[options](string)

