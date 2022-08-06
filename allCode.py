'''
# factorial
enter = int(input("Enter your number : "))
factorial = 1

if enter < 0:
    print("Sorry factorial does not")
elif enter == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, enter + 1):
        factorial = factorial * i
    print("The factorial of",enter,"is",factorial)
'''

'''
# Find n-th fibonacci number

def fabonacci(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fabonacci(n-1)+fabonacci(n-2)

print(fabonacci(10))
'''

'''
# Check if a number is prime or not

primeNumber = int(input("Enter your prime number : "))

flag = False

if primeNumber > 1:
    for i in range (2, primeNumber):
        if (primeNumber % i) == 0:
            flag = True
            break
if flag:
    print(primeNumber, "is not a prime number")
else:
    print(primeNumber, "is a prime number")
'''

'''
# Rotate a list by n places (accept list, and integer as input)

number = int(input("Enter your number : "))
listOne = [1, 2, 3, 4, 5, 6]
if number > len(listOne):
    number = int(number % len(listOne))
listOne = (listOne[-number:] + listOne[:-number])

print(listOne)
'''

'''
# Find all characters that appear more than once in a string

checkString = 'aaaaa'
count = {}

for s in checkString:
    if s in count:
        count[s] += 1
    else:
        count[s] = 1
for key in count:
    if count[key] > 1:
        print(key , count[key])
'''

'''
# Replace all occurrences of a word in a string (accepted as input the word u want to replace)

enterString = input("Enter your string : ")
str = "Hey guys how are you and how is your going on"
str = str.replace(enterString, '$')
print(str)
'''

'''
# Accept some text as input and print all words in descending order of their occurrence

enterText = input("Enter your text : ")
def descText(s):
    s.sort(reverse= True)
    str1 = ''.join(s)
    print(str1)

def newFunc():
    s = list(enterText)

    descText(s)

if __name__=="__main__":
    newFunc()
'''

'''
# Check if a year is a leap year or not

year = int(input("Enter your year : "))
if (year % 400 == 0 ) and (year % 100 == 0):
    print("{0} is leap year".format(year))
if (year % 4 == 0) and (year % 100 != 0):
    print("{0} is leap year : ".format(year))
else:
    print("{0} is not a leap year : ".format(year))
'''

'''
# 1 - Create ordered dictionary from an unordered dictionary

from collections import OrderedDict

domain = OrderedDict([('de', 'Germany'),
                      ('sk', 'Slovakia'),
                      ('hu', 'Hungary'),
                      ('us', 'United States'),
                      ('no', 'Norway')])
print('domain', domain)
'''


# 2 - Create ordered dictionary from an unordered dictionary




