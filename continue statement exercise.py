"""
Continue Statement Exercises:
1. Write a Python program to print all the even numbers between 1 and 20 except for the number 10 using a for loop and continue statement.

print('even numbers between 1 and 20 except 10')
for i in range(1,21):
    if i % 2 == 0:
        if i == 10:
            continue
        print(i)

=============================================================================================================================================
2. Write a Python program to print the elements of a list skipping the negative numbers using a while loop and continue statement.


list = [1,2,3,5,6,7,-3,-7,5,-7,4,-6,-8]
i = 0
while i < len(list):
    if list[i] < 0:
        i += 1
        continue
    print(list[i])
    i += 1

=====================================================================================================================================
3. Write a Python program to print the first 10 multiples of 3 except for the number 9 using a for loop and continue statement.

for i in range(1,11):
    x = i * 3
    if x == 9 :
        continue
    print(x)

======================================================================================================================================
4. Write a Python program to iterate over a string and print only the consonants using a for loop and continue statement.


str = input('Enter a string: ')
str.lower()
for i in str:
    if i in ('a','e','i','o','u') :
        continue
    print(i)

============================================================================================================================================
5. Write a Python program to print the elements of a list skipping the even numbers using a while loop and continue statement.

list1 = list(range(1,11))
i = 0
while i < len(list1):
    if i % 2 == 0 :
        i += 1
        continue
    print(i)
    i += 1

===================================================================================================================================================
6. Write a Python program to find the sum of all numbers between 1 and 100, excluding the multiples of 5 using a for loop and continue statement.

l1 = range(1,101)
sum = 0
for i in l1:
    if i % 5 == 0 :
        continue
    sum += i
print('Sum of all numbers excluding the multiples of 5 : ',sum)

=======================================================================================================================================================
7. Write a Python program to print the uppercase letters in a string using a while loop and continue statement.

str = input('Enter a string: ')
i = 0
while i < len(str):
    if str[i].islower() or str[i] == ' ':
        i += 1
        continue
    print(str[i])
    i += 1

===================================================================================================================================================
8. Write a Python program to print the elements of a list skipping the elements divisible by 3 using a for loop and continue statement.

l1 = list(map(int,input('Enter space separated number: ').split()))
for i in l1:
    if i % 3 == 0:
        continue
    print(i)

======================================================================================================================================================
9. Write a Python program to iterate over a list of tuples and print only the tuples with a specific condition using a while loop and continue statement.

list = [('python'),('pdf'),('script'),('java'),('c++'),('physics'),('mech'),('cse')]
i = 0
while i < len(list):
    if len(list[i]) > 4:
        i += 1
        continue
    print(list[i])
    i += 1

============================================================================================================================================================
10. Write a Python program to print the numbers from 1 to 50, skipping the multiples of 7 using a for loop and continue statement.


l1 = range(1,51)
for i in l1:
    if i % 7 == 0 :
        continue
    print(i)

=================================================================================================================================================================
"""
