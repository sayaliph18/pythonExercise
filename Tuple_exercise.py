"""

1. Write a Python program to find the length of a tuple.

def length(t1):
    return len(t1)
t1 = tuple(map(int,input('Enter a tuple separated by space: ').split()))
print(t1)
print('Length of tuple: ',length(t1))

===================================================================================
2. Write a Python program to concatenate two tuples.

def con(t1,t2):
    return (t1+t2)
t1 = tuple(map(int,input('Enter a tuple separated by space: ').split()))
print(t1)
t2 = tuple(map(int,input('Enter a tuple separated by space: ').split()))
print(t2)
print('concatenation two tuples: ',con(t1,t2))

===================================================================================
3. Write a Python program to convert a tuple to a list.

def convert(t1):
    return list(t1)
t1 = tuple(map(int,input('Enter a tuple separated by space: ').split()))
print(t1)
print('converting a tuple to a list: ',convert(t1))

=================================================================================
4. Write a Python program to find the index of an element in a tuple.

def index_no(t1):
    return t1.index(n)
t1 = tuple(map(int,input('Enter a tuple separated by space: ').split()))
print(t1)
n = int(input('Enter a element to check: '))
print ('Index of given element: ',index_no(t1))


====================================================================================
5. Write a Python program to check if an element exists in a tuple.

t1 = tuple(map(int,input('Enter a tuple separated by space: ').split()))
print(t1)
n = int(input('Enter a element you want to check: '))
if n in t1:
    print('Element exist in a tuple')
else:
    print('Element not exist in a tuple')


========================================================================================
6. Write a Python program to count the number of occurrences of an element in a tuple.

def count_number(t1):
    return t1.count(n)
t1 = tuple(map(int,input('Enter a tuple separated by space: ').split()))
print(t1)
n = int(input('Enter a element you want to check: '))
print('Occurrences of  given element : ',count_number(t1))

=========================================================================================
7. Write a Python program to find the maximum and minimum elements in a tuple.

t1 = tuple(map(int,input('Enter a number by space separated: ').split()))
print(t1)
print('Maximum elements in a tuple : ',max(t1))
print('Minimum elements in a tuple: ',min(t1))

======================================================================================
8. Write a Python program to reverse a tuple.

def reverse(t1):
    return t1[::-1]
t1 = tuple(map(int,input('Enter a tuple separated by space: ').split()))
print(t1)
print('reverse a tuple: ',reverse(t1))

=======================================================================================
9. Write a Python program to check if all elements in a tuple are the same.

def check(t1,t2):
    if t1 == t2:
        print('All elements are same')
    else:
        print('All elements are not same')
t1 = tuple(map(int,input('Enter a tuple separated by space: ').split()))
print(t1)
t2 = tuple(map(int,input('Enter a tuple separated by space: ').split()))
print(t2)
check(t1,t2)

=========================================================================================
10. Write a Python program to create a new tuple with the elements from two existing tuples.


def con(t1,t2):
    return (t1+t2)
t1 = tuple(map(int,input('Enter a tuple separated by space: ').split()))
print(t1)
t2 = tuple(map(int,input('Enter a tuple separated by space: ').split()))
print(t2)
print('concatenation two tuples: ',con(t1,t2))

=============================================================================================
"""
