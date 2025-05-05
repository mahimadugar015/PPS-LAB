#Write a Python program to calculate the average marks for 5 subjects. The program should prompt the user to input the marks for each subject. After receiving the input, it should compute the average marks and then determine the corresponding grade based on the following grading system:
#A: 90 - 100
#B: 80 - 89
#C: 70 - 79
#D: 60 - 69
#F: Below 60

sum = 0
n = 5
for i in range(1,n+1):
	marks = float(input(f"subject {i}: ",))
	sum = sum + marks
	avg = sum/5.0
print(f"Average Marks: {avg:.2f}")

if(avg >= 90):
	print("Grade: A\n")
elif(avg < 89 and avg > 80):
	print("Grade: B\n")
elif(avg < 79 and avg > 70):
	print("Grade: C\n")
elif(avg < 69 and avg > 60):
	print("Grade: D\n")
else:
	print("Grade: F\n")