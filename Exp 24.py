#Write a python program to define a module to find Fibonacci Numbers and import the module to another program.

import fibonacci_module

def main():
	try:
		n = int(input("Enter the max value: "))
		if n>0:
			fib = fibonacci_module.generate_fibonacci_sequence(n)
			print(f"Fibonacci series upto {n} :")
			print(" ".join(map(str,fib)),end =" ")
		else:
			print("Please enter a positive integer")
	except ValueError :
		print("Invalid input! Please enter a valid integer.")
		

if __name__ == "__main__":
	main()
	