import random

def encrypt():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']
    key = open('key.txt', 'r')
    key = str(key.read())
    plain = open('plainText.txt', 'r')
    plain = str(plain.read())
    plain = plain.lower()
    cipher = open('cipherText.txt', 'w')

    alphaLen = len(alphabet)-1
    textLen = len(plain)
    start = random.randint(0, len(key)-1-textLen)
    keyString = key[start:start+textLen]
    cipherText = ""
    augment = ""

    for i in range(textLen):			
        textIndex = alphabet.index(plain[i])
        keyIndex = alphabet.index(keyString[i])
        if textIndex +2*(keyIndex) == (alphaLen):
            cipherText += "`"
            
        elif textIndex and keyIndex == (alphaLen):
            cipherText += alphabet[(textIndex+keyIndex)-(alphaLen)]
            
        elif textIndex == (alphaLen):
            cipherText += alphabet[textIndex-keyIndex]
            
        elif keyIndex == (alphaLen):
            cipherText += alphabet[textIndex]
            
        elif (textIndex+keyIndex) > (alphaLen):
            cipherText += alphabet[(textIndex+keyIndex)-(alphaLen)]
            
        else:
            cipherText += alphabet[(textIndex+keyIndex)]
        
    for i in range(len(str(len(str(key))))-len(str(start))):
        augment += "0"
    augment += str(start)
    cipherText = augment + cipherText
    cipher.write(cipherText)
    cipher.close()
