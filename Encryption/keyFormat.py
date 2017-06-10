import random

def reformat():
	readText = open('PlutarchLives.txt', 'r')
	writeText = open('key.txt', 'w')
	readText = str(readText.read())
	readText = readText.replace('\n', '')
	readText = readText.lower()
	for i in range(len(readText)):
		if readText[i] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']:
			readText = readText.replace(readText[i], random.choice('abcdefghiklmnopqrstuvwxyz1234567890'))
	writeText.write(readText)
	writeText.close()
	print("Complete")
