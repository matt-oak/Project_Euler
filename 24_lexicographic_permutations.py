#Project Euler Problem #24
#Lexicographic Permutations

import itertools

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
i = 1

for permutation in itertools.permutations(nums, len(nums)):
	if i == 1000000:
		print "".join(permutation),
		break
	i += 1