#Write a program to print the sum of digits of a number.

def sum(num):
	sum = 0 
	while num > 0 :
		sum += num % 10
		num //=10
	return sum

n = int(input("num: "))
print("sum:",sum(n))