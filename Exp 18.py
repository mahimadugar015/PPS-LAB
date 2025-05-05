#Write a Python program to find whether a given string is a palindrome or not.

def check(str):
	if str == str[::-1]:
		return "palindrome"
	else:
		return "not a palindrome"

s = input()
print(check(s))