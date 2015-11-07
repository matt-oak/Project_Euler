import sys

def main(argv):
	f = open("names.txt", "r")
	word_list = []
	for words in f.read().split(','):
		words = words[1:-1]
		word_list.append(words)
	word_list.sort()
	summation = 0
	for i in range(0, len(word_list)):
		count = string_to_count(word_list[i])
		summation = summation + ((i+1)*count)
	print summation
	
	return

def string_to_count(string):
	count = 0
	for i in range(0, len(string)):
		if string[i] == 'A':
			count = count + 1
		elif string[i] == 'B':
			count = count + 2
		elif string[i] == 'C':
			count = count + 3
		elif string[i] == 'D':
			count = count + 4
		elif string[i] == 'E':
			count = count + 5
		elif string[i] == 'F':
			count = count + 6
		elif string[i] == 'G':
			count = count + 7
		elif string[i] == 'H':
			count = count + 8
		elif string[i] == 'I':
			count = count + 9
		elif string[i] == 'J':
			count = count + 10
		elif string[i] == 'K':
			count = count + 11
		elif string[i] == 'L':
			count = count + 12
		elif string[i] == 'M':
			count = count + 13
		elif string[i] == 'N':
			count = count + 14
		elif string[i] == 'O':
			count = count + 15
		elif string[i] == 'P':
			count = count + 16
		elif string[i] == 'Q':
			count = count + 17
		elif string[i] == 'R':
			count = count + 18
		elif string[i] == 'S':
			count = count + 19
		elif string[i] == 'T':
			count = count + 20
		elif string[i] == 'U':
			count = count + 21
		elif string[i] == 'V':
			count = count + 22
		elif string[i] == 'W':
			count = count + 23
		elif string[i] == 'X':
			count = count + 24
		elif string[i] == 'Y':
			count = count + 25
		elif string[i] == 'Z':
			count = count + 26
	return count
		
if __name__ == "__main__":
	main(sys.argv)
