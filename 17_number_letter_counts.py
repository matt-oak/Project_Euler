# imports
import sys
import math


# main function
def main(argv):
	summation = 0
	#one ... ninety nine
	for i in range(1, 100):
		summation = summation + to_words(i)
	#854 characers for 1 - 99
	#print summation
	#one hundred and ...
	one_hundreds = (13*99)+summation+10
	two_hundreds = (13*99)+summation+10
	three_hundreds = (15*99)+summation+12
	four_hundreds = (14*99)+summation+11
	five_hundreds = (14*99)+summation+11
	six_hundreds = (13*99)+summation+10
	seven_hundreds = (15*99)+summation+12
	eight_hundreds = (15*99)+summation+12
	nine_hundreds = (14*99)+summation+11
	thousand = 11
	
	total = summation + one_hundreds + two_hundreds + three_hundreds + four_hundreds + five_hundreds + six_hundreds + seven_hundreds + eight_hundreds + nine_hundreds + thousand
	print total


	return
#insert other functions here
def to_words(num):
	count = 0
	char = str(num)
	if char == "10":
		count = count + 3
		return count
	elif char == "11":
		count = count + 6
		return count
	elif char == "12":
		count = count + 6
		return count
	elif char == "13":
		count = count + 8
		return count
	elif char == "14":
		count = count + 8
		return count
	elif char == "15":
		count = count + 7
		return count
	elif char == "16":
		count = count + 7
		return count
	elif char == "17":
		count = count + 9
		return count
	elif char == "18":
		count = count + 8
		return count
	elif char == "19":
		count = count + 8
		return count
		
	if char == "20":
		count = count + 6
		return count
	elif char == "30":
		count = count + 6
		return count
	elif char == "40":
		count = count + 5
		return count
	elif char == "50":
		count = count + 5
		return count
	elif char == "60":
		count = count + 5
		return count
	elif char == "70":
		count = count + 7
		return count
	elif char == "80":
		count = count + 6
		return count
	elif char == "90":
		count = count + 6
		return count
		
	if char == "1":
		count = count + 3
		return count
	elif char == "2":
		count = count + 3
		return count
	elif char == "3":
		count = count + 5
		return count
	elif char == "4":
		count = count + 4
		return count
	elif char == "5":
		count = count + 4
		return count
	elif char == "6":
		count = count + 3
		return count
	elif char == "7":
		count = count + 5
		return count
	elif char == "8":
		count = count + 5
		return count
	elif char == "9":
		count = count + 4
		return count
	
	if char[len(char) - 2] == "2":
		count = count + 6
		for i in range(1, 10):
			if i == int(char[len(char) - 1]):
				count = count + to_words(i)
				return count
	elif char[len(char) - 2]  == "3":
		count = count + 6
		for i in range(1, 10):
			if i == int(char[len(char) - 1]):
				count = count + to_words(i)
				return count
	elif char[len(char) - 2]  == "4":
		count = count + 5
		for i in range(1, 10):
			if i == int(char[len(char) - 1]):
				count = count + to_words(i)
				return count
	elif char[len(char) - 2]  == "5":
		count = count + 5
		for i in range(1, 10):
			if i == int(char[len(char) - 1]):
				count = count + to_words(i)
				return count
	elif char[len(char) - 2]  == "6":
		count = count + 5
		for i in range(1, 10):
			if i == int(char[len(char) - 1]):
				count = count + to_words(i)
				return count
	elif char[len(char) - 2]  == "7":
		count = count + 7
		for i in range(1, 10):
			if i == int(char[len(char) - 1]):
				count = count + to_words(i)
				return count
	elif char[len(char) - 2]  == "8":
		count = count + 6
		for i in range(1, 10):
			if i == int(char[len(char) - 1]):
				count = count + to_words(i)
				return count
	elif char[len(char) - 2]  == "9":
		count = count + 6
		for i in range(1, 10):
			if i == int(char[len(char) - 1]):
				count = count + to_words(i)
				return count
		
	
	

# maint entry point
if __name__ == "__main__":
	main(sys.argv)
