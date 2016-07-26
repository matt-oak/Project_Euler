#Project Euler Problem #29
#Distinct Powers

power_list = []

for i in range(2, 101):
	for j in range(2, 101):
		num = i ** j
		if num not in power_list:
			power_list.append(num)

print len(power_list)