#Project Euler Problem #35
#Circular Primes

#Check if the number is prime
def is_prime(x):
	prime = True
	for i in range(2, x/2 + 1):
		if x % i == 0:
			prime = False
			break
		else:
			continue

	return prime

#Return rotation of list 'x'
def rotate(x, n):
	return x[n:] + x[:n]

#Iterate through all odd numbers < 1,000,000
circ_primes = 1
for i in range(3, 1000000, 2):
	if i < 10:
		if is_prime(i):
			circ_primes += 1
		continue

	#If there is an even integer in the number disregard it
	if "8" in str(i) or "6" in str(i) or "4" in str(i) or "2" in str(i) or "0" in str(i):
		continue

	chars = list(str(i))
	num_rotations = len(chars)
	circ_check = 0

	#Iterate through all rotations of the string and see if it is prime
	for j in range(1, num_rotations + 1):
		rotation = rotate(chars, j)
		string = ''.join(rotation)
		num = int(string)
		if is_prime(num):
			circ_check += 1
		else:
			break

	#If all rotations are prime, add 1 to circ_prime accumulator
	if circ_check == num_rotations:
		print ''.join(chars)
		circ_primes += 1

print circ_primes
