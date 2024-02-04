"""
1. Write a Python program to iterate over a range of numbers and print them.

print('Numbers in given range:')
for i in range(1,21):
    print(i)

===============================================================================
2. Write a Python program to find the sum of all numbers in a range.

print('sum of all numbers:')
sum_1 = sum(range(1,5))
print(sum_1)

==============================================================================
3. Write a Python program to print all even numbers in a given range.

print('Even numbers in given range:')
for i in range(1,21):
    if i % 2 == 0:
        print(i)

=============================================================================
4. Write a Python program to print all odd numbers in a given range.

print('Odd numbers in given range:')
for i in range(1,21):
    if i % 2 != 0:
        print(i)

=============================================================================
5. Write a Python program to find the average of all numbers in a range.

print('average of all numbers in a range:')
avg_1 = sum(range(1,5))/len(range(1,5))
print(avg_1)

=============================================================================
6. Write a Python program to check if a number is present in a given range.

x = range(1,100)
y = int(input('Enter a number: '))
if y in x:
    print('number is present in a given range')
else:
    print('number is not present in a given range')

===============================================================================
7. Write a Python program to reverse a range of numbers and print them.

print('Reverse numbers in given range:')
for i in range(10,0,-1):
    print(i)

===============================================================================
8. Write a Python program to find the product of all numbers in a range.

print('product of  numbers in given range:')
prod = 1
for i in range(1,11):
    prod = prod * i
print(prod)

===============================================================================
9. Write a Python program to print the squares of all numbers in a range.

print('product of  numbers in given range:')
for i in range(1,11):
    print('Square of',i,':',i*i)


===============================================================================
10. Write a Python program to print the cube of all numbers in a range.


print('product of  numbers in given range:')
for i in range(1,11):
    print('Cube of',i,':',i*i*i)

===============================================================================
"""
