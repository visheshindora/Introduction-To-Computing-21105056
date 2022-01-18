# ASSIGNMENT-2


# 1st Program



print("Ques.1}\n\n")

a = input("Type Your String: ")  # a = String
# a is the string enter by user


# Part (a)

lenght = len(a)
print("\na. Lenght of the entered string is:", lenght, "\n")


# Part (b)

rev = (a[::-1])   #Reversed
print("b. Reversed Order of String:", rev, "\n")


# Part (c)

new_str = a[10:26]
print("c. New String is:", new_str, "\n")


# Part (d)

X = a.replace(new_str, "object oriented")
print("d. Repalced String is:", X, "\n")

# Part (e)

sub_index = a.index("a")     #Substring
print("e. Index of Substring 'a' is:", sub_index, "\n")

# Part 5

no_space = a.replace(" ", "")
print("Your String with no spaces", no_space)










# 2nd PROGRAM




print("\n\n\n\n\nQues.2}\n\n")
name = "Vishesh Indora"
sid = 21105056
dept = "ECE"
cg = 8.5     #CGPA

print("Hey,", name, "Here!\n"
                    "My SID is", sid, "\n"
                                      "I am from", dept, "Department and my CGPA is", cg)










# 3rd Program

print("\n\n\n\n\nQues.3}\n\n")
a = 56
b = 10

print("a = ", a, "\n",
      "b = ", b)
# Part (a)

print("a. a&b = ", a & b,"\n")

# Part (b)

print("b. a|b = ", a | b, "\n")

# Part(c)

print("c. a^b = ", a ^ b, "\n")

# Part (d)

print("d. Left Shift of 'a' by 2 bits = ", a << 2, "\n",
      "  Left Shift of 'b' by 2 bits = ", b << 2)

# Part (e)

print("e. Right Shift of 'a' by 2 bits = ", a >> 2, "\n"
      "   Right Shift of 'b' by 4 bits = ", b >> 4)










# Program 4


print("\n\n\n\n\nQues.4}\n\n")

print("Enter three numbers to find the greatest number:-")

# Number to be enter by the user
a = float(input("First Number = "))
b = float(input("Second Number = "))
c = float(input("Third Number = "))

if a >= b and a >= c:
    greatest = a
elif b >= c:
    greatest = b
else:
    greatest = c

print("\nGreatest Number is:", greatest)










# PROGRAM 5


print("\n\n\n\n\nQues.5}\n\n")
print("Enter a sentence to know wheather it contain 'name'or not:-\n")

sen = input("Enter Your Sentence: ")  #Sentence
remark = "Does this sentence contain word 'name' :"

if "name" in sen:
    print("\n", remark, "Yes")
else:
    print("\n", remark, "No")










# PROGRAM 6

print("\n\n\n\n\nQues.6}\n\n")

print("Enter three lengths to se wheather a triangle can be formed from these lenghts or not:-\n")
x = float(input("Length of First Side of Triangle = "))
y = float(input("Length of Second Side of Trisngle = "))
z = float(input("Length of Third Side of Triangle = "))


if x >= y+z or y >= x+z or z >= x+y :
     print("\nNo, Triangle can't be formed.")
else:
     print("\nYes, Triangle can be formed.")
