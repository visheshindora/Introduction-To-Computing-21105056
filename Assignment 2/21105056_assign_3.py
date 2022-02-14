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
