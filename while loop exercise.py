"""
While Loop Exercises:
1. Write a Python program to print the numbers from 1 to 10 using a while loop.


i = 1
while i <= 10:
    print(i)
    i += 1

========================================================================================================
2. Write a Python program to calculate the sum of all numbers from 1 to 100 using a while loop.

i = 0
sum = 0
while i <= 100:
    sum += i
    i += 1
print("sum of all numbers from 1 to 100 : ",sum)

========================================================================================================
3. Write a Python program to find the factorial of a number using a while loop.

x = int(input('Enter a number: '))
i = 1
fact = 1
while i <= x:
    fact *= i
    i += 1
print("factorial of a number : ",fact)

========================================================================================================
4. Write a Python program to print all the even numbers between 1 and 50 using a while loop.

print('even numbers between 1 and 50 : ')
i = 1
while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1

========================================================================================================
5. Write a Python program to iterate over a string and print each character using a while loop.

str = input('Enter a str: ')
i = 0
while i < len(str):
    print(str[i])
    i += 1

=======================================================================================================
6. Write a Python program to iterate over a list of tuples and print each element using a while loop.

t1 = [(1,2),(3,4),(4,5),(6,7)]
i = 0
while i < len(t1):
    print(t1[i])
    i += 1

========================================================================================================
7. Write a Python program to find the largest element in a list using a while loop.

t1 = [1,2,3,4,5,6]
largest = -99999
i = 0
while i < len(t1):
    if t1[i] > largest:
        largest = t1[i]
    i += 1
print('Largest element in a list : ',largest)

=========================================================================================================
8. Write a Python program to check if all elements in a list are even using a while loop.

t1 = [1,2,3,4,5,6]
status = 'all elements in a list are even'
i = 1
while i <= len(t1):
    if i % 2 != 0:
        status = 'all elements in a list are not even'
    i += 1
print(status)

=====================================================================================================
9. Write a Python program to find the common elements between two lists using a while loop.

def find_common(list1, list2):
    list1.sort()
    list2.sort()
    common_elements = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            common_elements.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return common_elements

list1 = [1,2,3,4,5,6]
list2 = [5,6,7,8,9]

common_elements = find_common(list1, list2)
print("Common elements:", common_elements)

==============================================================================================================
10. Write a Python program to calculate the sum of the digits of a number using a while loop.

def find_digitsum(n):
    if n < 10:
        return n
    digitsum = 0
    while n > 0:
        digitsum = digitsum + (n % 10)
        n = n//10
    return digitsum
num = int(input('Enter a number : '))
print('Digit sum is: ',find_digitsum(num))

=================================================================================================================
"""




