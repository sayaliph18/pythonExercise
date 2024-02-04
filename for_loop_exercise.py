"""
For Loop Exercises:
1. Write a Python program to print the numbers from 1 to 10 using a for loop.

for i in range(1,11):
    print(i)


=======================================================================================================
2. Write a Python program to calculate the sum of all numbers in a list using a for loop.

list1 = list(range(1,11))
sum = 0
for i in list1:
    sum += i
print('Sum of all numbers: ',sum)

==========================================================================================================
3. Write a Python program to find the factorial of a number using a for loop.

num = int(input('Enter a number: '))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print('Factorial of a number: ',fact)

============================================================================================================
4. Write a Python program to print all the even numbers between 1 and 50 using a for loop.

print('Even numbers between 1 and 50 : ')
for i in range(1,51):
    if i % 2 ==0:
        print(i)

=========================================================================================================
5. Write a Python program to iterate over a string and print each character using a for loop.


str = input('Enter a string: ')
for i in str:
    print(i)

=========================================================================================================
6. Write a Python program to iterate over a list of tuples and print each element using a for loop.

tup = [(1,2),(3,4),(5,6)]
for i in tup:
    for j in i:
        print(j)

=========================================================================================================
7. Write a Python program to find the largest element in a list using a for loop.

def find_largest(list):
    if not list:
        return 'List is empty'
    largest = -999999
    for i in list:
        if i > largest:
            largest = i
    return 'Largest element is :', largest
list = [1,2,3,4,5,6,7,8,9]
print(*find_largest(list))


===========================================================================================================
8. Write a Python program to check if all elements in a list are even using a for loop.

List = list(map(int,input('Enter a space separated list :  ').split()))
for i in List:
    if i % 2 == 0:
        print(i,'is even number')

===========================================================================================================
9. Write a Python program to find the common elements between two lists using a for loop.

l1 = [1,2,3,4,5,6]
l2 = [5,6,7,8,9,5]
com = []
for i in set(l1):
    for j in set(l2):
        if i == j:
            com.append(i)
print('common elements between two lists: ',com)

=============================================================================================================
10. Write a Python program to calculate the sum of the digits of a number using a for loop.


num = int(input('Enter a number: '))
digit_sum = 0
for i in str(num):
    digit_sum += int(i)
print('Sum of digits: ',digit_sum)

=============================================================================================================
"""

