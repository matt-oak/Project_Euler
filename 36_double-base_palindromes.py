#Project Euler Problem 36
#Double-base Palindromes

total = 0
for i in range(1, 1000000):
	num = str(i)
	bin_num = str(bin(i)[2:])

	if num == num[::-1] and bin_num == bin_num[::-1]:
		total = total + int(num)

print total