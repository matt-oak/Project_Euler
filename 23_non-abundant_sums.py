#Project Euler Problem 23
#Non-abundant Sums

def all_nums():
	num_list = []
	for i in range(1, 28124):
		num_list.append(i)
	return num_list


def factor(num):
	factors = []
	for i in range(1, ((num / 2) + 1)):
		if num % i == 0:
			factors.append(i)
		else:
			continue
	return factors

def abundant_numbers():
	abundant_nums = []
	for i in range(1, 28124):
		factors = factor(i)
		summation = 0
		for j in range(0, len(factors)):
			summation = summation + factors[j]
		if summation > i:
			abundant_nums.append(i)
		else:
			continue

	return abundant_nums

def abundant_sums(abundant_nums, all_nums):
	for i in range(0, len(abundant_nums)):
		for j in range(i, len(abundant_nums)):
			summation = abundant_nums[i] + abundant_nums[j]
			if summation in all_nums:
				all_nums.remove(summation)

	total = 0
	for i in range(0, len(all_nums)):
		total = total + all_nums[i]

	print total


num_list = all_nums()
abundant_nums = abundant_numbers()
abundant_sums(abundant_nums, num_list)