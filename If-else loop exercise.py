"""
If-Else Loop Exercises:
1. Write a Python program to check if a number is positive, negative, or zero.

num = int(input('Enter a number: '))
if num == 0:
    print('Number is zero')
elif (num > 0):
    print('Number is positive')
else:
    print('Number is negative')

=======================================================================================
2. Write a Python program to check if a number is even or odd.

num = int(input('Enter a number: '))
if (num % 2 == 0):
    print('Number is even')
else:
    print('Number is odd')

========================================================================================
3. Write a Python program to check if a year is a leap year or not.

year = int(input('Enter a year: '))
if (year % 4 == 0):
    print(year ,'is a leap year')
else:
    print(year ,'is not a leap year')

========================================================================================
4. Write a Python program to find the maximum of three numbers using if-else.

num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))
num3 = int(input('Enter a number: '))
if (num1 > num2) and (num1 > num3):
    print(num1,'is maximum of three numbers')
elif (num2 > num1) and (num2 > num3):
    print(num2,'is maximum of three numbers')
else:
    print(num3,'is maximum of three numbers')


=========================================================================================
5. Write a Python program to check if a number is prime.

num = int(input('Enter a number: '))
if num == 1:
    print(num,'is not a prime number')
elif (num>1):
    for i in range(2,num):
        if (num % i)==0:
            print(num,'is not a prime number')
            break
    else:
            print(num, 'is a prime number')
else:
    print(num, 'is not a prime number')

=======================================================================================
6. Write a Python program to check if a number is divisible by both 3 and 5.

num = int(input('Enter a number: '))
if (num % 3==0) and (num % 5==0):
    print(num,' is divisible by both 3 and 5')
else:
    print(num, ' is not divisible by both 3 and 5')

=========================================================================================
7. Write a Python program to check if a character is a vowel or consonant.

str = input('Enter a number: ')
s1 = str.lower()
if s1 in ['a','e','i','o','u']:
    print(s1,'is a vowel')
else:
    print(s1,'is consonant')

=========================================================================================
8. Write a Python program to check if a given string is a palindrome using if-else.

str = input('Enter a number: ')
if str ==  str[::-1]:
    print(str,'is a palindrome')
else:
    print(str,'is not a palindrome')

=======================================================================================================
9. Write a Python program to determine the largest among three numbers using nested if-else.

num1 = int(input('Enter a number: '))
num2 = int(input('Enter a number: '))
num3 = int(input('Enter a number: '))
if (num1 > num2):
    if (num1 > num3):
        print(num1,'is maximum of three numbers')
    else:
        print(num3,'is maximum of three')
else:
    if (num2 > num3):
        print(num2,'is maximum of three numbers')
    else:
        print(num3,'is maximum of three numbers')

=========================================================================================================
10. Write a Python program to check if a triangle is equilateral, isosceles, or scalene based on its side lengths using if-else.

s1 = int(input('Enter a length: '))
s2 = int(input('Enter a length: '))
s3 = int(input('Enter a length: '))
if (s1 == s2 == s3):
   print('triangle is equilateral')
elif (s1==s2) or (s2==s3) or(s1==s3):
    print('triangle is isosceles')
else:
    print('triangle is scalene')

==========================================================================================================
"""
