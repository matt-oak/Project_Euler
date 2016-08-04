#Project Euler Problem #33
#Digit Cancelling Fractions

from __future__ import division

numerators = []
denominators = []

for i in range(10, 100):
	for j in range(10, 100):
		if i > j:
			continue
		i_str = str(i)
		j_str = str(j)
		if i_str[0] == j_str[0]:
			new_num = int(i_str[1])
			new_den = int(j_str[1])
		elif i_str[0] == j_str[1]:
			new_num = int(i_str[1])
			new_den = int(j_str[0])
		elif i_str[1] == j_str[0]:
			new_num = int(i_str[0])
			new_den = int(j_str[1])
		elif i_str[1] == j_str[1]:
			new_num = int(i_str[0])
			new_den = int(j_str[0])
		else:
			continue

		quotient = i / j
		if new_den == 0:
			continue
		mini_quotient = new_num / new_den

		if quotient == mini_quotient and quotient != 1 and i_str[1] != '0':
			numerators.append(i)
			denominators.append(j)

big_num = 1
big_den = 1
for i in range(0, len(numerators)):
	big_num = big_num * numerators[i]
	big_den = big_den * denominators[i]

print "Numerator:", big_num
print "Denominator:", big_den
print "Reduced Denominator:", big_den / big_num


