#Project Euler Problem #27
#Quadratic Primes

import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    if n < 0:
    	return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_all_primes(a, b):
	num_primes = 0
	n = 0
	stopper = True
	while stopper == True:
		number = n**2 + (a * n) + b
		if is_prime(number) == True:
			num_primes += 1
			n += 1
			continue
		break
	return num_primes

max_number_primes = 0
x = 0
y = 0
for a in range(-999, 999):
	for b in range(-999, 999):
		num_primes = get_all_primes(a, b)
		if num_primes > max_number_primes:
			max_number_primes = num_primes
			x = a
			y = b
print x * y
