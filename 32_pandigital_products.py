#Project Euler Problem #32
#Pandigital Products

pandigitals = []
for i in range(0, 9999):
	for j in range(0, 99):
		digit_list = []
		product = i * j
		x = str(i)
		y = str(j)
		prod = str(product)
		for k in range(0, len(x)):
			digit_list.append(x[k])
		for k in range(0, len(y)):
			digit_list.append(y[k])
		for k in range(0, len(prod)):
			digit_list.append(prod[k])
		if len(digit_list) == len(set(digit_list)) and len(digit_list) == 9 and '0' not in x and '0' not in y and '0' not in prod:
			if prod not in pandigitals:
				pandigitals.append(prod)

summation = 0
for i in range(0, len(pandigitals)):
	summation = summation + int(pandigitals[i])

print summation