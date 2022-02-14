# Q1


print('Q1\n')

given = input("Enter your string: ").lower()


def frequency(given):
    if " " not in given:
        list1 = []
        for words in given:
            if words not in list1:
                count = 0
                for i in range(len(given)):
                    if given[i] == words:
                        count += 1
                    list1.append(words)
                print(f"{words} - {count}")
    else:
        list2 = []
        list = given.split()
        for word in list:
            if word not in list2:
               count = 0
               for i in range(len(list)):
                   if list[i] == word:
                       count += 1
                   list2.append(word)
               print(f"{word} - {count}")
frequency(given)





# Q2

print("Q2\n")

print("Enter:-")
date = int(input("Date: "))
month = int(input("Month: "))
year = int(input("Year: "))

non_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap = [31,29,31,30,31,30,31,31,30,31,30,31]
def next_date():
    if year in range(1800,2026) and month in range(1,13):
        if year%4 == 0:
            if (date + 1) <= leap[month - 1]:
                print(f"Next date: {date + 1}/{month}/{year}")
            elif date == leap[month - 1]:
                if month == 12:
                    print(f"Next date: {1}/{1}/{year+1}")
                else:
                    print(f"Next date: {1}/{month+1}/{year}")
            else:
                print('The date not valid')
        else:
            if (date + 1) <= non_leap[month - 1]:
                print(f"Next date: {date + 1}/{month}/{year}")
            elif date == non_leap[month - 1]:
                if month == 12:
                    print(f"Next date: {1}/{1}/{year+1}")
                else:
                    print(f"Next date: {1}/{month+1}/{year}")
            else:
                print('The date not valid')
    else:
        print("year or month is not valid")
next_date()






# Q3
print("Q3\n")

def square():
    no_element = int(input("Enter number of elements: "))
    list=[]
    for i in range(no_element):
        element = int(input("enter element: "))
        list.append(element)

    list2=[]
    for i in range(no_element):
        list2.append((list[i], list[i] ** 2))
    print(list2)
square()






# Q4
print("Q4\n")

def grades():
    grade = int(input("Enter Your Grade: "))

    if grade == 10:
        print("Your grade is A+ \nOutstanding Performance.")
    elif grade == 9:
        print("Your grade is A \nExcellent Performance.")
    elif grade == 8:
        print("Your grade is B+ \nVery Good Performance.")
    elif grade == 7:
        print("Your grade is B \nGood Performance.")
    elif grade == 6:
        print("Your grade is C+ \nAverage Performance.")
    elif grade == 5:
        print("Your grade is C \nBelow Average Performance.")
    elif grade == 4:
        print("Your grade is D \nPoor Performance.")
    else:
        print("Enter a valid grade")
grades()






# Q5
print("Q5\n")

def pattern():
    word = 'ABCDEFGHIJK'

    for i in range(6):
        print(word)
        word= " " + word[0:len(word) - 2]
pattern()





# Q6

print('Q6\n')

def data_structure():
    data = {}
    condition = "y"
    while condition == "y" or condition == "Y":
        name = input("Enter Name: ")
        sid = int(input('Enter SID: '))

        data[sid] = name

        condition = input("Weather you want to enter name and SID <y/n>: ").lower()
        if condition=="n":
            break

    print("Q6a\n")
    print('A. The dictionary is:\n', data)

    print("Q6b\n")
    data_items=data.items()
    data_sort = sorted(data_items)

    data = dict(data_sort)

    print('B. After sorting:\n', data)

    print("Q6c")
    SID=int(input('Enter SID: '))
    print("C. Name of student with SID", SID,"is: ", data[SID])
data_structure()





