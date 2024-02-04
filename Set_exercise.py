"""

Set Exercises:
1. Write a Python program to find the union of two sets.

s1 = set(map(int,input('Enter space separated numbers: ').split()))
print(s1)
s2 = set(map(int,input('Enter space separated numbers: ').split()))
print(s2)
print('Union of two sets : ',s1.union(s2))

============================================================================
2. Write a Python program to find the intersection of two sets.

s1 = set(map(int,input('Enter space separated numbers: ').split()))
print(s1)
s2 = set(map(int,input('Enter space separated numbers: ').split()))
print(s2)
print('Intersection of two sets : ',s1.intersection(s2))

===========================================================================
3. Write a Python program to check if a set is a subset of another set.

s1 = set(map(int,input('Enter space separated numbers: ').split()))
print(s1)
s2 = set(map(int,input('Enter space separated numbers: ').split()))
print(s2)
print('Set is a subset of another set : ',s1.issubset(s2))

============================================================================
4. Write a Python program to remove duplicate elements from a set.

s1 = set(map(int,input('Enter space separated numbers: ').split()))
print('After removing duplicates : ',s1)

============================================================================
5. Write a Python program to add an element to a set.

s1 = set(map(int,input('Enter space separated numbers: ').split()))
print(s1)
num = int(input('Enter a element you want to add: '))
s1.add(num)
print('Updated set : ',s1)

==============================================================================
6. Write a Python program to remove an element from a set.

s1 = set(map(int,input('Enter space separated numbers: ').split()))
print(s1)
num = int(input('Enter a element you want to remove: '))
s1.remove(num)
print('Updated set : ',s1)

==============================================================================
7. Write a Python program to find the difference between two sets.

s1 = set(map(int,input('Enter space separated numbers: ').split()))
print(s1)
s2 = set(map(int,input('Enter space separated numbers: ').split()))
print(s2)
print('difference of two sets : ',s1.difference(s2))

================================================================================
8. Write a Python program to check if two sets are disjoint.

s1 = set(map(int,input('Enter space separated numbers: ').split()))
print(s1)
s2 = set(map(int,input('Enter space separated numbers: ').split()))
print(s2)
print('two sets are disjoint : ',s1.isdisjoint(s2))

==================================================================================
9. Write a Python program to find the symmetric difference between two sets.

s1 = set(map(int,input('Enter space separated numbers: ').split()))
print(s1)
s2 = set(map(int,input('Enter space separated numbers: ').split()))
print(s2)
print('symmetric difference of two sets : ',s1.symmetric_difference(s2))

=================================================================================
10. Write a Python program to check if a set is empty.

s1 = set(map(int,input('Enter space separated numbers: ').split()))
print(s1)
if not s1:
    print('Set is empty')
else:
    print('Set is not empty')

====================================================================================
"""

