#Write a program to count the number of vowels using sets in a given string.

def vowel_count(str):
	count = 0
	vowel = set("aeiouAEIOU")
	for ch in str:
		if ch in vowel:
			count += 1
	print(count)
	# Write your code here to count the vowels
	
str = input()
vowel_count(str)