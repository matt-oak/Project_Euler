# imports
import sys
import math


# main function
def main(argv):
	x = str(pow(2, 1000))
	summation = 0
	for i in range(0, len(x)):
		summation = summation + int(x[i])
	print summation


	return
#insert other functions here

# maint entry point
if __name__ == "__main__":
	main(sys.argv)
