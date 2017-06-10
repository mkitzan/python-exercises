def decrypt():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']
    key = open('key.txt', 'r')
    key = str(key.read())
    cipher = open('cipherText.txt', 'r')
    cipher = str(cipher.read())
    plain = open('plainText.txt', 'w')

    alphaLen = len(alphabet)-1
    start = int(cipher[:len(str(len(str(key))))])
    cipher = cipher[7:len(cipher)]
    textLen = len(cipher)
    keyString = key[start:start+textLen]
    plainText = ""

    for i in range(textLen):			
        keyIndex = alphabet.index(keyString[i])
        if cipher[i] == '`':
            plainText += alphabet[(alphaLen) - (keyIndex*2)]
        else:
            textIndex = alphabet.index(cipher[i])
            if keyIndex == (alphaLen):
                plainText += alphabet[textIndex]
                
            elif textIndex+keyIndex == (alphaLen):
                plainText += alphabet[textIndex+keyIndex]

            elif textIndex > keyIndex:
                plainText += alphabet[textIndex-keyIndex]
                      
            elif textIndex < keyIndex:
                plainText += alphabet[(textIndex-keyIndex)+(alphaLen)]

            else:
                plainText += alphabet[keyIndex-textIndex]

    plain.write(plainText)
    plain.close()
