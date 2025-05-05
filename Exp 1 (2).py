#Write a program to calculate the area of a circle and print the result as shown in the displayed test cases.

rad = float(input("Enter the radius : "))
pi = 3.14
area = pi * rad * rad
if rad >= 0.0 and rad < 100.0:
	print("Area of circle =",format(area,".6f"))
	#print("Area of circle =%6f",area)
else:
	print("Enter a positive value upto 100\n")