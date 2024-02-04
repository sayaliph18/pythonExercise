"""
Break Statement Exercises:
1. Write a Python program to find the first occurrence of a number in a list using a for loop and break statement.


list = [2,4,5,6,7,8,3,9]
num = 8
for i in range(len(list)):
    if list[i] == num:
        print('first occurrence of a number : ',i)
        break

======================================================================================================================
2. Write a Python program to search for a specific element in a list using a while loop and break statement.


def find_element(n, list):
    i = 0
    while i < len(list):
        if list[i] == n:
            print(f'Number {n} is present in list at {i+1} position.')
            break
        i += 1
    if i == len(list) and i != n:
        print(f'Number {n} is not present in list')
    return

list = [2,4,5,6,7,8,3,9]
num = int(input('Enter number to search in list: '))
find_element(num, list)

=======================================================================================================================
3. Write a Python program to find the prime numbers between 1 and 100 using a for loop and break statement.


primelist = []
for i in range(1,101):
    if i == 1:
        continue
    if i == 2:
        primelist.append(i)
        continue
    for j in range(2,i):
        if i % j == 0:
            break
    if j == i-1:
        primelist.append(i)
print(primelist)


=============================================================================================================================
4. Write a Python program to check if a number is present in a list using a while loop and break statement.

def find_element(n, list):
    i = 0
    while i < len(list):
        if list[i] == n:
            print(f'Number {n} is present in list at {i+1} position.')
            break
        i += 1
    if i == len(list) and i != n:
        print(f'Number {n} is not present in list')
    return

list = [2,4,5,6,7,8,3,9]
num = int(input('Enter number to search in list: '))
find_element(num, list)

=====================================================================================================================
5. Write a Python program to find the largest palindrome number in a given range using a for loop and break statement.

def is_palindrome(n):
    if str(n) == str (n)[::-1]:
        return  1
    return None
palindrome = -1
for i in range(2000,3000):
    if is_palindrome(i):
        if i >palindrome:
            palindrome = i
print('Largest palindrome in given range is: ',palindrome)

========================================================================================================================
6. Write a Python program to find the first negative number in a list using a while loop and break statement.

list = [2,4,5,6,-3,7,8,3,9,-4]
i = 0
while i < len(list):
    if list[i] < 0:
        print('First negative number in the list is: ',list[i])
        break
    i += 1

========================================================================================================================
7. Write a Python program to print the elements of a list until a specific condition is met using a for loop and break statement.

list = [2,4,5,6,-3,7,8,3,9,-4]
for i in list:
    print(i)
    if i % 5 == 0:
        print('condition is met ')
        break

========================================================================================================================
8. Write a Python program to search for a specific character in a string using a while loop and break statement.

str = 'Python is programming language'
char = input('Enter char to search: ')[0]
i = 0
while i < len(str):
    if str[i] == char:
        print(f'Char {char} is present in string at index {i}.')
        break
    i += 1
else:
    print(f'Char {char} is not present in given string.')


=================================================================================================================================
9. Write a Python program to find the first occurrence of a vowel in a string using a for loop and break statement.

str = 'Python is programming language'
for i in str.lower():
    if i in ['a','e','i','o','u']:
        print('Vowel is present at index',str.lower().index(i))
        break

==================================================================================================================================
10. Write a Python program to find the index of the first occurrence of a substring in a string using a while loop and break statement.


def search_substring(string, substr):
    x =len(substr)
    index = -1
    i = 0
    while i < len(string)-x:
        if string[i:i+x] == substr:
            index = i
            break
        i += 1
    return index

string = 'India is my country. All indians are my brothers and sisters.'
substr = 'and'
res = search_substring(string, substr)
if res != -1:
    print(f'Substring present at index {res}')
else:
    print('Substring not present.')


===================================================================================================================
"""
