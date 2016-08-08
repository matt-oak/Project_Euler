#Project Euler Problem #40
#Champernowne's Constant

num_sequence = ""
for i in range(1, 200000):
	num_sequence = num_sequence + str(i)

nums = []
nums.append(int(num_sequence[0]))
nums.append(int(num_sequence[9]))
nums.append(int(num_sequence[99]))
nums.append(int(num_sequence[999]))
nums.append(int(num_sequence[9999]))
nums.append(int(num_sequence[99999]))
nums.append(int(num_sequence[999999]))

prod = 1
for i in range(0, len(nums)):
	prod = prod * nums[i]

print prod