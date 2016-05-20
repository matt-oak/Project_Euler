def divisors(x):
	divs = []
	acc = 0
	for i in range (1, x):
		if x % i == 0:
			divs.append(i)
	for j in range(0, len(divs)):
		acc = acc + divs[j]
	return acc
	
amicables = 0
acc = 0
for i in range(1, 10000):
	acc1 = divisors(i)
	acc2 = divisors(acc1)
	if i == acc2:
		if i != acc1:
			print i, acc1
			acc = acc + i
print "-------------------------------"
print "total: " + str(acc)