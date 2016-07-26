#Project Euler Problem #25
#1000-digit Fibonacci Number

fib_numbers = []
x = 1
y = 1
fib_numbers.append(x)
fib_numbers.append(y)

for i in range(2, 5000):
	addition = fib_numbers[i - 2] + fib_numbers[i - 1]
	fib_numbers.append(addition)
	length = len(str(addition))
	if length == 1000:
		print i + 1
		exit()
