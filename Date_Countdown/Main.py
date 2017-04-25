import datetime
import time

current_date = datetime.date.today()
with open("Saved_dates.txt", "r") as saved_dates:
	saved_lines_of_dates = saved_dates.readlines()

def date_checker(string, date_type):
	if date_type == "year":
		try:
			datetime.date(int(string), 1, 1)
		except ValueError:
			return False
	elif date_type == "month":
		try:
			datetime.date(1, int(string), 1)
		except ValueError:
			return False
	elif date_type == "day":
		try:
			datetime.date(int(year_string), int(month_string), int(string))
		except ValueError:
			return False
	return True

def ask_reask(keyword):
	input_string = input(keyword.capitalize() + "? - ")

	while date_checker(input_string, keyword) == False:
		input_string = input("This is not a proper " + keyword + ".\nTry again - ")

	return input_string

def string_dates_to_diffs(year_str, month_str, day_str, current_date):
	event_date = datetime.date(int(year_str), int(month_str), int(day_str))
	return (event_date - current_date)

for i in range(0, int(len(saved_lines_of_dates)/4)):
	if len(saved_lines_of_dates) > 0:
		date_diff = string_dates_to_diffs(saved_lines_of_dates[4*i + 1], saved_lines_of_dates[4*i + 2], saved_lines_of_dates[4*i + 3], current_date)
		print(saved_lines_of_dates[4*i] + str(date_diff.days) + " days.\n")

print("What date (in digit form) do you wish to count down until/since?\n")

while True:
	year_string = ask_reask("year")
	month_string = ask_reask("month")
	day_string = ask_reask("day")

	time_difference = string_dates_to_diffs(year_string, month_string, day_string, current_date)

	if time_difference.days < 0:
		print(str(time_difference.days * -1) + " days have passed since this this date!\n")
	elif time_difference == 0:
		print("Wow! Seems like you are very bad at maff. This date is today.\n")
	else:
		print("You have " + str(time_difference.days) + " days left until this date!\n")

	time.sleep(2)

	to_save_switch = input("Would you like to save this date. Then, next time you run the program, the number of days will be culculated automatically. To save the date, enter 's'. Otherwise, enter anything.\n")
	if to_save_switch == "s":
		date_description = input("How do you wish to name your date?\n")
		with open("Saved_dates.txt", "r+") as saved_dates:
			if len(saved_dates.readlines()) > 0:
				is_empty_file = False
			else:
				is_empty_file = True

		if is_empty_file == True:
			with open("Saved_dates.txt", "w") as saved_dates:
				saved_dates.write(date_description + "\n" + year_string + "\n" + month_string + "\n" + day_string + "\n")
		else:
			with open("Saved_dates.txt", "a") as saved_dates:
				saved_dates.write(date_description + "\n" + year_string + "\n" + month_string + "\n" + day_string + "\n")
		print("Your date was successfully saved! You will see the countdown the next time you open the program.\n")

	time.sleep(2)

	stop_or_continue = input("If you wish to find out how many days are left before anothere date, enter anything. Otherwise, enter 'c' to close the program.\n")
	if stop_or_continue == "c":
		break

#To be implemented:
#	- allow closing by force and still saving the dates
#	- store dates as dictionaries
#	- converting the number of days to other units
#	- prevent storing the same data
#	~ print each word with a small delay
