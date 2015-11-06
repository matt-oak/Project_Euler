import sys
import math

def main(argv):
	x = math.factorial(100)
	x_str = str(x)
	summation = 0
	for i in range(0, len(x_str) - 1):
		num1 = int(x_str[i])
		summation = summation + num1
	print summation

	return

if __name__ == "__main__":
	main(sys.argv)
