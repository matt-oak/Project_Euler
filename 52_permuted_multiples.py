#Project Euler Problem #52
#Permuted Multiples

answers = []

for i in range(100, 167):
	ones = sorted(list(str(i)))
	twice = sorted(list((str(i * 2))))
	thrice = sorted(list((str(i * 3))))
	fours = sorted(list((str(i * 4))))
	fives = sorted(list((str(i * 5))))
	sixes = sorted(list((str(i * 6))))

	if ones == twice and ones == thrice and ones == fours and ones == fives and ones == sixes:
		answers.append(i)

if len(answers) > 0:
	print answers[0]
	exit()

for i in range(1000, 1670):
	ones = sorted(list(str(i)))
	twice = sorted(list((str(i * 2))))
	thrice = sorted(list((str(i * 3))))
	fours = sorted(list((str(i * 4))))
	fives = sorted(list((str(i * 5))))
	sixes = sorted(list((str(i * 6))))

	if ones == twice and ones == thrice and ones == fours and ones == fives and ones == sixes:
		answers.append(i)

if len(answers) > 0:
	print answers[0]
	exit()

for i in range(10000, 16700):
	ones = sorted(list(str(i)))
	twice = sorted(list((str(i * 2))))
	thrice = sorted(list((str(i * 3))))
	fours = sorted(list((str(i * 4))))
	fives = sorted(list((str(i * 5))))
	sixes = sorted(list((str(i * 6))))

	if ones == twice and ones == thrice and ones == fours and ones == fives and ones == sixes:
		answers.append(i)

if len(answers) > 0:
	print answers[0]
	exit()

for i in range(100000, 167000):
	ones = sorted(list(str(i)))
	twice = sorted(list((str(i * 2))))
	thrice = sorted(list((str(i * 3))))
	fours = sorted(list((str(i * 4))))
	fives = sorted(list((str(i * 5))))
	sixes = sorted(list((str(i * 6))))

	if ones == twice and ones == thrice and ones == fours and ones == fives and ones == sixes:
		answers.append(i)

if len(answers) > 0:
	print answers[0]
	exit()

for i in range(1000000, 1670000):
	ones = sorted(list(str(i)))
	twice = sorted(list((str(i * 2))))
	thrice = sorted(list((str(i * 3))))
	fours = sorted(list((str(i * 4))))
	fives = sorted(list((str(i * 5))))
	sixes = sorted(list((str(i * 6))))

	if ones == twice and ones == thrice and ones == fours and ones == fives and ones == sixes:
		answers.append(i)

print answers[0]