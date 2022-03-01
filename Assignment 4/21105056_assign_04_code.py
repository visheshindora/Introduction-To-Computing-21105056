# Q1

print("\nQ1\n\n")


def tower_of_hanoi(n, selected_rod, destination_rod, centeral_rod):
	if n == 0:
		return
	tower_of_hanoi(n - 1, selected_rod, centeral_rod, destination_rod)
	print(f"Move disk {n} selected the rod {selected_rod} destination of rod {destination_rod}")
	tower_of_hanoi(n - 1, centeral_rod, destination_rod, selected_rod)


n = 3
tower_of_hanoi(n, 'A', 'C', 'B')






# Q2

print("\n\n\n\n\nQ2\n\n")


from math import factorial

n = int(input('Enter the size of pascals triangle you want: '))

print("Pascal Triangle with Loop")

for i in range(n):
    for j in range(n - i + 1):
        print(end=" ")  # space between triangle

    for j in range(i + 1):
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")  # nCr = n!/((n-r)!*r!)
    print()  # for new line

print("\n\nPascal Triangle with Recurssions")


def pascal_triangle(n, original_length=n):
    if n == 0:
        return
    pascal_triangle(n - 1, original_length)
    print(' ' * (original_length - n), end=' ')  # for print the spaces(" ")
    begin = 1  # first number is always 1
    for i in range(1, n + 1):
        print(begin, end=" ")

        begin = begin * (n - i) // i  # using Binomial Coefficient
    print()


pascal_triangle(n)





# Q3

print("\n\n\n\n\nQ3\n\n")


int_1=int(input("First number: "))
int_2=int(input("Second number: "))

quotient = int_1 // int_2
remainder = int_1 % int_2

# Q3a

print("\n(a) Checking whether the quotient and remainder is a callable value or not")
print(callable(quotient))
print(callable(remainder))


# Q3b

if (quotient == 0):
    print("(b) The quotient is zero")
if (remainder == 0):
    print("(b) The reminder is zero")
if (quotient != 0 and remainder != 0):
    print("(b) All the values are non zero")


# Q3c

partClist = [quotient + 4, remainder + 4, remainder + 5, quotient + 5, remainder + 5, quotient + 6, remainder + 6]

result = []
for i in range(len(partClist)):
    if partClist[i] > 4:
        result.append(partClist[i])
print(f"(c) Filtered out numbers that are greater than 4 are : {result}")

#part (d)
set_result = set(result)
print("(d) Set:",set_result)

#part (e)
immutable_Set = frozenset(set_result) #frozen Set is used to make the set immutable
print("(e) Immutable set:",immutable_Set)

#part (f)
print("(f) Hash value of the maximum value from the above set:", hash(max(immutable_Set)))





# Q4


print("\n\n\n\n\nQ4\n\n")


class Student:
    def __init__(self, student, roll_no):
        self.name = student
        self.roll_no = roll_no

    def __del__(self):
        print("Object destroyed")


# creating object
student_1 = Student("Vishesh Indora", 21105056)
print("Object created")  # printing the assigned values
print(f"The name of the student it {student_1.name} and SID is {student_1.roll_no}.")
del student_1  # deleting object





# Q5


print("\n\n\n\n\nQ5\n\n")


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# creating employee records
employ_1 = Employee("Mehak", 40000)
employ_2 = Employee("Ashok", 50000)
employ_3 = Employee("Viren", 60000)

# Q5a (updating salary)

employ_1.salary = 70000
print(f"(a)The updated salary of {employ_1.name} is {employ_1.salary} ")


# Q5b (deleting a record)

del employ_3
print("(b)Record of Viren has been removed", end='')






# Q6


print("\n\n\n\n\nQ6\n\n")


# inputting a word from the first friend
word = input("Enter the word: ").lower()

# inputting a meaningful word with the exact same letters
test_word = input("Enter a word using the exact same letters to test your friendship: ").lower()


# defining dictionary
def count_in_dict(word):
    count = {}
    list1 = list(word)

    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count


# shopkeeper's input to verify the word's meaning
def userinput():
    if count_in_dict(word) != count_in_dict(test_word):
        print("The letters aren't exact, friendship is fake")
        return
    ans = input("Does the word makes sense? (Y/N): ").lower()

    if ans == 'y':
        print("The friends pass the friendship test")
    elif ans == 'n':
        print("The word doesn't have a meaning, friendship is fake")
    else:
        print("Invalid input,try again with Y/N ")
        userinput()


userinput()
