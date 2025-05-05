#Take an integer n from the user. Your task is to Write a program to find out the sum of the digits of the given number using the process of recursion. Print the result as shown in the Test cases. 

def Sumof(n):
	if n == 0 :
		return 0
	else:
		return n % 10 + Sumof( n // 10 )

# take user input and add the function call
n = int(input())
print(Sumof(n))