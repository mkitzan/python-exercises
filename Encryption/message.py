def newMessage():
	plain = open('plainText.txt', 'w')
	message = input("Enter message: ")
	plain.write(message)
	plain.close

def printMessage():
        text = open('plainText.txt', 'r')
        text = str(text.read())
        print(text)

def printCipher():
        text = open('cipherText.txt', 'r')
        text = str(text.read())
        print(text)
