#Write a Python program to perform union, intersection and difference operations on Set A and Set B.

import math

a = list(map(int,input("Set A: ").split()))
A = set(a)
b = list(map(int,input("Set B: ").split()))
B = set(b)

# Write your code here to perform different operations

union = A.union(B)
print("Union: ",union)

inter = A.intersection(B)
print("Intersection: ",inter)

differ = A.difference(B)
print("Difference: ",differ)