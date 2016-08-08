#Project Euler Problem #43
#Sub-string Divisibility

import itertools

def create_permutations(num_list):
	perms = list(itertools.permutations(num_list))
	return perms

pandigital = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
perms = create_permutations(pandigital)

summation = 0
for i in range(0, len(perms)):
	seq = str(''.join(map(str,perms[i])))
	div_2 = int(seq[1:4])
	div_3 = int(seq[2:5])
	div_5 = int(seq[3:6])
	div_7 = int(seq[4:7])
	div_11 = int(seq[5:8])
	div_13 = int(seq[6:9])
	div_17 = int(seq[7:10])

	if div_2 % 2 == 0 and div_3 % 3 == 0 and div_5 % 5 == 0 and div_7 % 7 == 0 and div_11 % 11 == 0 and div_13 % 13 == 0 and div_17 % 17 == 0:
		summation = summation + int(seq)

print summation