#Write a Python program that prompts the user to input a date (year, month, and day) and checks if it is a valid date. If the entered date is valid, the program should increment the date by one day and display the incremented date. The program should take into account leap years when determining the number of days in February.

import datetime

def Date(year,month,day):
	try:
		date = datetime.date(year,month,day)
		inc = date + datetime.timedelta(days=1)
		return f"valid\nincremented date: {inc}"
	except ValueError :
		return "invalid"

year = int(input("year: "))
month = int(input("month: "))
day = int(input("day: "))

print(Date(year,month,day))