#!/usr/bin/python3
# Coded by: Alex Rocha
# Contact: lecoverde10@gmail.com
#

import base64
import hashlib
import os
import time

def clear():

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def title():
    print('''\n============ CHOOSE HASH TYPE ============
[1] SHA1        [3] MD5         [5] Base64
[2] SHA256      [4] SHA512      [6] Exit
==========================================\n''')

def main():

    clear()
    while True:
        string = input("Type the text to be encoded: ")
        title()
        options = int(input("\nSelect the option: "))
        
        time.sleep(1)
        if options < 1 or options > 6:
            print("Invalid option\n")
            continue

        elif options == 1:
            clear()
            result = hashlib.sha1(string.encode('utf-8'))
            print(f"\nSHA1: {result.hexdigest()}")
            print()
            repeat = input("Do you want to encript another text (y/n)? ")
            if repeat.lower() == 'y':
                clear()
                continue
            elif repeat.lower() == 'n':
                print()
                time.sleep(0.5)
                print("End Program.")
                break
            else:
                print()
                print("Invalid option.")
                break

        elif options == 2:
            clear()
            result = hashlib.sha256(string.encode('utf-8'))
            print(f"\nSHA256: {result.hexdigest()}")
            print()
            repeat = input("Do you want to encript another text (y/n)? ")
            if repeat.lower() == 'y':
                clear()
                continue
            elif repeat.lower() == 'n':
                print()
                time.sleep(0.5)
                print("End Program.")
                break
            else:
                print()
                print("Invalid option.")
                break

        elif options == 3:
            clear()
            result = hashlib.md5(string.encode('utf-8'))
            print(f"\nMD5: {result.hexdigest()}")
            print()
            repeat = input("Do you want to encript another text (y/n)? ")
            if repeat.lower() == 'y':
                clear()
                continue
            elif repeat.lower() == 'n':
                print()
                time.sleep(0.5)
                print("End Program.")
                break
            else:
                print()
                print("Invalid option.")
                break

        elif options == 4:
            clear()
            result = hashlib.sha512(string.encode('utf-8'))
            print(f"\nSHA512: {result.hexdigest()}")
            print()
            repeat = input("Do you want to encript another text (y/n)? ")
            if repeat.lower() == 'y':
                clear()
                continue
            elif repeat.lower() == 'n':
                print()
                time.sleep(0.5)
                print("End Program.")
                break
            else:
                print()
                print("Invalid option.")
                break

        elif options == 5:
            clear()
            result = base64.b64encode(string.encode('utf-8'))
            result_encoded = result.decode('utf-8')
            print(f"\nBase64: {result_encoded}")
            print()
            repeat = input("Do you want to encript another text (y/n)? ")
            if repeat.lower() == 'y':
                clear()
                continue
            elif repeat.lower() == 'n':
                print()
                time.sleep(0.5)
                print("End Program.")
                break
            else:
                print()
                print("Invalid option.")
                break

        elif options == 6:
            print("End program.")
            time.sleep(1)
            clear()
            break

if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print("\nInvalid character. Type a number between 1 and 6.")
    except Exception as error:
        print(f"\nError: {str(error)}")
    except KeyboardInterrupt:
        time.sleep(0.5)
        print("\n\nEnd program!")
    
