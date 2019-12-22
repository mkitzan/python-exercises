
from os import listdir
from os.path import isfile, join
from sys import argv

def pattern(file, key):
	num = 1
	lines = []
	try:
		with open(file) as source:
			for line in source:
				# track line numbers
				if key in line:
					lines += [num]
				num += 1
		# print matching line numbers for the file
		if lines != []:
			print("Pattern matched at:\t" + file)
			for num in lines:
				print("\t" + str(num))
			print()
	except:
		# catches parsing exceptions
		return


def search(dir, key, check):
	for file in listdir(dir):
		pos = join(dir, file)
		# recurse next folder
		if not isfile(pos):
			search(pos, key, check)
		# pattern search files matching extension
		elif check(pos):
			pattern(pos, key)


def main():
	if len(argv) != 4:
		print("python search.py <directory> <pattern> <extension>")
		return
	search(argv[1], argv[2], lambda file: (argv[3] == "*" or file[-len(argv[3]):] == argv[3]))


if __name__ == "__main__":
	main()
