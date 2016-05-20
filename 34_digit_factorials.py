import math

final_acc = 0
for i in range(1, 100000):
	str_num = str(i)
	acc = 0
	for j in range(0, len(str_num)):
		num = int(str_num[j])
		fact = math.factorial(num)
		acc = acc + fact
	if acc == i and i != 1 and i != 2:
		print i
		final_acc = final_acc + i
		
print "answer: ", final_acc