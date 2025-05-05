#Write a Python program that prompts the user to input three digits (0-9) and checks if the entered digits are valid. If the digits are valid, the program generates all possible combinations of these three digits and prints them. Each combination is formed by arranging the digits in different orders. If the input is not valid (digits are not between 0 and 9), the program should display as "Invalid".

import itertools

a = int(input("digit1 (0-9): "))
b = int(input("digit2 (0-9): "))
c = int(input("digit3 (0-9): "))

if(0 <= a <= 9) and (0 <= b <= 9) and (0 <= c <= 9):
	com = itertools.permutations([a,b,c])
	for combo in com :
		print(''.join(map(str,combo)))

else:
	print("Invalid")