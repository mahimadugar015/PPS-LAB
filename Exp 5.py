#Write a Python program to find the roots of a quadratic equation by taking the coefficients from the user.

import cmath

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = (b**2) - (4*a*c)

if(d > 0):
	r1 = (-b + cmath.sqrt(d))/(2*a)
	r2 = (-b - cmath.sqrt(d))/(2*a)
	print(f"The roots are: {r1.real:.2f} and {r2.real:.2f}")
elif d == 0 :
	root = -b/ (2*a)
	print(f"The root is: {root:.2f}")
else:
	r1 = (-b + cmath.sqrt(d))/(2*a)
	r2 = (-b - cmath.sqrt(d))/(2*a)

	real1 = f"{r1.real:.2f}"
	imag1 = f"{r1.imag:.2f}"
	real2 = f"{r2.real:.2f}"
	imag2 = f"{r2.imag:.2f}"

	if float(real1) == 0.0 :
		real1 = "-0.00"

	print(f"The roots are: {real1}+{imag1}j and {real2}{imag2}j")
