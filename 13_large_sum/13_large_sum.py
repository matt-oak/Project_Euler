# imports
import sys


# main function
def main(argv):
	num_list = []
	total = 0
	f = open("nums2.txt", 'r')
	for lines in f:
		num_list.append(lines)
	for i in range(0, len(num_list)):
		num_list[i] = num_list[i].replace('\n', '')
	#print num_list
	num_length = 50
	total = 100
	biggy = []
	remainder = 0
	for i in range(0, 5):
		summation = 0
		for j in range(0, total):
			item = num_list[j]
			char = int(item[num_length - 1 - i])
			summation = summation + char
		print "Initial Summation: ", summation
		summation = summation + int(remainder)
		sum_to_string = str(summation)
		keeper = int(sum_to_string[len(sum_to_string) - 1])
		biggy.append(keeper)
		remainder = sum_to_string[:-1]
		print "Summation: ", summation
		print "Keeper: ", keeper
		print "Biggy: ", biggy
		print "Remainder: ", remainder
		if i == num_length - 1:
			biggy.append(summation)
	biggy.reverse()
	print len(biggy)
			
		
	
	
	
	
	return
#insert other functions here

# maint entry point
if __name__ == "__main__":
	main(sys.argv)
