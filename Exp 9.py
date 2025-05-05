#Write a Python program to check if a given year is a leap year or not.

yr = int(input("Enter a year: "))
if(yr % 4 == 0):
	print(yr,"is a leap year")
else:
	print(yr,"is not a leap year")
