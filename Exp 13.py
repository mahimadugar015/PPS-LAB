#Write a Python program to print the following pattern.

def pattern(n):
	for i in range(n,0,-1):
		print('* '*i)

try:
	num = int(input("Enter a number : "))
	if num <= 0 :
		print("Please enter a positive number")
	else:
		pattern(num)
except ValueError:
	print("Invalid input! Please enter a valid integer.")