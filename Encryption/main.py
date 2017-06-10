from os import *
import keyFormat
import encrypt
import decrypt
import message

def main():
    print("Select action: \nnew message/encrypt(1) \ndecrypt/print message(2) \nprint cipher text(3)")
    action = input()
    if action == '1':        
        message.newMessage()
        encrypt.encrypt()
    elif action== '2':
        decrypt.decrypt()
        message.printMessage()
    elif action == '3':
        message.printCipher()
    elif action == 'format':
        keyFormat.reformat()
    else:
        main()
    print()
    input('press enter to continue')
    system('cls')
    main()
main()
