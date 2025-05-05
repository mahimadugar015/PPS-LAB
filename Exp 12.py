#Write a python program to print factorial of given number.

def factorial(n):
	if n == 0:
		return 1
	else:
		result = 1
		for i in range(1, n+1):
			result *= i
		return result

try:
	num = int(input("Enter a number : "))
	if num < 0 :
		print("Enter a positive number")
	else:
		print(f"Factorial of given number is : {factorial(num)}")
except ValueError:
	print("Invalid input! Please enter a valid integer.")