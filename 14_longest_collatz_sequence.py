#imports
import sys

# main function
def main(argv):
	totes = []
	for i in range(13, 1000000):
		sequence = []
		num = i
		stopper = True
		while stopper == True:
			if num == 1:
				#print sequence
				totes.append(len(sequence))
				if len(sequence) == 524:
					print i
				stopper = False
			elif num % 2 == 0:
				num = num >> 1
				sequence.append(num)
			elif num % 2 != 0:
				num = num + num + num + 1
				sequence.append(num)
	print max(totes)
	
	
	
	
	return
#insert other functions here

# maint entry point
if __name__ == "__main__":
	main(sys.argv)
