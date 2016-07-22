#Project Euler Problem 19
#Counting Sundays

def get_num_days():
	days_in_year = 365
	days_in_leap_year = 366
	num_years = 100
	num_leap_years = num_years / 4
	non_leap_year_days = (num_years - num_leap_years) * days_in_year
	leap_year_days = num_leap_years * days_in_leap_year
	total_days = non_leap_year_days + leap_year_days

	return total_days


def build_day_list(total_num_days):
	day_list = []

	for i in range(0, total_num_days):
		if i % 7 == 5:
			day_list.append('Sun')
		else:
			day_list.append('x')

	return day_list

def get_sundays(day_list):
	sundays = 0

	for year in range(0, 100):
		for month in range(0, 12):
			if day_list[0] == 'Sun':
				sundays += 1
			if month == 1 and (year + 1) % 4 == 0:
				day_list = day_list[29:]
			elif month == 1:
				day_list = day_list[28:]
			elif month == 3 or month == 5 or month == 8 or month == 10:
				day_list = day_list[30:]
			else:
				day_list = day_list[31:]

	return sundays


total_num_days = get_num_days()
day_list = build_day_list(total_num_days)
num_sundays = get_sundays(day_list)
print "Total number of Sundays falling on the first of the month in the 20th century:", num_sundays