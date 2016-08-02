#Project Euler Problem #30
#Digit Fifth Powers

ans_list = []
for i in range(2, 1000000):
	str_digit = str(i)
	digit_list = []

	for j in range(0, len(str_digit)):
		digit_list.append(str_digit[j])
	
	summation = 0
	for j in range(0, len(digit_list)):
		num = int(digit_list[j])**5
		summation = summation + num

	if i == summation:
		ans_list.append(i)

summation = 0
for i in range(0, len(ans_list)):
	summation = summation + ans_list[i]

print summation