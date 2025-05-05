#Write a Python program that prints prime numbers less than n which represents the upper limit.

def prime_s(n):
	if n <= -1 :
		return False
	for i in range (2,int(n** 0.5) + 1):
		if n%i==0:
			return False
	else:
		return True

def print_s(limit):
	for n in range(2,limit):
		if prime_s(n):
			print(n)

n = int(input("Enter upper limit: "))
print_s(n)