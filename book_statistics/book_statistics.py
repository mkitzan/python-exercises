
import sys
import math

class Book:
	def __init__(self, author, year, pages):
		self.author = author
		self.year = int(year)
		self.pages = int(pages)
		
class Aggregate:
	book_count = 0
	year_count = 0
	author_count = 0
	page_count = 0
	authors = {}	#a:[book#, page#, year[]]
	years = {} 	#y:[book#, page#]
	books = []
	
	def __init__(self):
		pass
	
	def n(self, arg):
		if arg == 'b':
			return self.book_count
		elif arg == 'a':
			return self.author_count
		elif arg == 'y':
			return self.year_count
		else:
			return -1
		
	def sum(self, arg):
		if arg == 'y': #test
			return sum([ k*self.years[k][0] for k in self.years.keys() ])
		elif arg == 'p':
			return self.page_count
		else:
			return -1
			
	def mean(self, arg):
		if arg == 'y':
			return self.sum('y') * 1.0 / self.book_count
		elif arg == 'p':
			return self.page_count * 1.0 / self.book_count
		else:
			return -1
	
	def sd(self, arg):
		xbar = self.mean(arg)
		n = 1
		sm = 0
		if arg == 'y':
			n = self.n(arg)-1
			sm = sum([ math.pow(x-xbar, 2)*self.years[x][0] for x in self.years.keys() ]) 
		elif arg == 'p':
			n = self.n('b')
			sm = sum([ math.pow(bk.pages-xbar, 2) for bk in self.books ]) 
		sm = sm * 1.0
		
		return math.sqrt(sm / n)
	
	def add_book(self, book):
		self.books.append(book)
		self.book_count += 1
		self.page_count += book.pages
		
		if book.author not in self.authors.keys():
			self.authors[book.author] = [0, 0, []]
			self.author_count += 1
		self.authors[book.author][0] += 1
		self.authors[book.author][1] += book.pages
		self.authors[book.author][2].append(book.year)
		
		if book.year not in self.years.keys():
			self.years[book.year] = [0, 0]
			self.year_count += 1
		self.years[book.year][0] += 1
		self.years[book.year][1] += book.pages
		
	def roundup(self, num, scale):
		return int(math.ceil(num / (scale * 1.0))) * scale
		
	def rounddown(self, num, scale):
		return int(math.floor(num / (scale * 1.0))) * scale
	
	def minmax(self, data, index):
		min = 999
		max = 0
		if data == 'y':
			for el in self.years.keys():
				n = self.years[el][index] 
				if n < min:
					min = n
				if n > max:
					max = n
		elif data == 'a':
			for el in self.authors.keys():
				n = self.authors[el][index] 
				if n < min:
					min = n
				if n > max:
					max = n
		elif data == 'b':
			for el in self.books:
				n = el.pages
				if n < min:
					min = n
				if n > max:
					max = n
		if index == 1:
			min = self.roundup(min, 100)
			max = self.roundup(max, 100)
	
		return (min, max)
	
			
	def plot(self, x_axis, y_axis):
		x_labels = []
		x_count = []
		y_labels = []
		y_minmax = (-1, -1)
		
		if x_axis == 'authors':
			x_labels = sorted(self.authors.keys())
			if y_axis == 'books':
				y_minmax = self.minmax('a', 0)
				x_count = [ self.authors[k][0] for k in x_labels ]
			else:
				y_minmax = self.minmax('a', 1)
				x_count = [ self.roundup(self.authors[k][1], 100) / 100 for k in x_labels ]
		elif x_axis == 'years':
			x_labels = sorted(self.years.keys())
			if y_axis == 'books':
				y_minmax = self.minmax('y', 0)
				x_count = [ self.years[k][0] for k in x_labels ]
			else:
				y_minmax = self.minmax('y', 1)
				x_count = [ self.roundup(self.years[k][1], 100) / 100 for k in x_labels ]
		else:
			return -1
		
		if y_axis == 'books':
			y_labels = [ n for n in range((y_minmax[1]) + 1) ]
		else:
			y_labels = [ n for n in range(int(y_minmax[1] / 100) + 1) ]
		y_labels.remove(0)
		
		print("   X: " + x_axis + "  Y: " + y_axis + "  Scale: " + (str(100) if y_axis == "pages" else str(1)))
		for i in reversed(y_labels):
			if i > 9:
				line = str(i) + "|"
			else:
				line = str(i) + " |"
			for j in range(len(x_count)):
				if x_count[j] == i:
					line += " * "
					x_count[j] -= 1
				else:
					line += "   "
			print(line)
		
		line = "   "
		for i in x_labels:
			line += "---"
		print(line)
		
		line = "   "
		if x_axis == 'years':
			x_labels = [ str(k)[2:] for k in x_labels ]
		else:
			x_labels = [ "".join([ n[0] for n in a if len(n) > 2 ]) for a in [ k.split() for k in x_labels ] ]
		line = "   "
		line += " ".join(x_labels)
		print(line)
		
def main():
	aggregator = Aggregate()
	
	with open(sys.argv[1], 'r') as infile:
		for line in infile:
			contents = line.split(',')
			current = Book(contents[0], contents[1], contents[2])
			aggregator.add_book(current)
	
	print("Total books read: 	" + str(aggregator.n('b')))
	print("Total pages read: 	" + str(aggregator.sum('p')))
	print("Unique pub years: 	" + str(aggregator.n('y')))
	print("Unique authors: 	" + str(aggregator.n('a')))
	print("Mean pub year: 		" + str(aggregator.mean('y')))
	print("Mean book length: 	" + str(aggregator.mean('p')))
	print("SD of pub years: 	" + str(aggregator.sd('y')))
	print("SD of book lengths: 	" + str(aggregator.sd('p')))
	mnmx = aggregator.minmax('b', -1)
	print("Shortest book:		" + str(mnmx[0]))
	print("Longest book:		" + str(mnmx[1]))
	print()
	aggregator.plot('authors', 'pages')
	print()
	aggregator.plot('authors', 'books')
	print()
	aggregator.plot('years', 'pages')
	print()
	aggregator.plot('years', 'books')
	
if __name__ == '__main__':
	main()