# Assignment 1


# 1st Program

print()
num1 = int(input("enter 1st number: "))
num2 = int(input("enter 2nd number: "))
num3 = int(input("enter 3rd number: "))
total = num1 + num2 + num3
avg = total/3
print("avg of numbers =", avg)


# 2nd Program

print()
tax_rate = 0.2                                                    # 20%
sd = 10000                                                        # Standard Deduction
dd = 3000                                                         # Dependent Deduction
gi = int(input("Enter Gross Income: "))                           # Gross Income
no_of_dependent = int(input("Enter No. Of Dependent: "))
taxable_income = gi - sd - (dd * no_of_dependent)
print("Taxable Income:", taxable_income)
tax = taxable_income * tax_rate
print("Tax:", tax)


# 3rd Program

print()
student = ["SID", "Name", "Gender", "Department Name", "CGPA"]
print("Student: ", student)
student = [21105056, "Vishesh Indora", "M", "ECE", 9.8]
print("student: ", student)


# 4th program

print()
marks = [63,96,78,36,52]
print("Marks Before Sorting: ", marks)
marks.sort()
print("Marks After Sorting: ", marks)


# 5th Program

print()
color = ['Red', 'Green', 'White', 'black', 'Pink', 'Yellow']
print("Color", color)
color.pop(3)
print("(a) Color", color)

color = ['Red', 'Green', 'White', 'black', 'Pink', 'Yellow']
color[3:5] = ["Purple"]
print("(b) Color", color)

