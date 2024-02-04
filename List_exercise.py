"""
1. Write a Python program to find the sum of all elements in a list.

List = list(map(int,input('Enter a number by space separated: ').split()))
print(List)
print('Sum of all elements in a list : ',sum(List))

--------------------------------------------------------------------------------------
2. Write a Python program to find the maximum and minimum elements in a list.

List = list(map(int,input('Enter a number by space separated: ').split()))
print(List)
print('Maximum elements in a list : ',max(List))
print('Minimum elements in a list : ',min(List))

--------------------------------------------------------------------------------------
3. Write a Python program to remove duplicates from a list.

List = list(map(int,input('Enter a number by space separated: ').split()))
print(List)
result = []
for i in List:
    if i not in result:
        result.append(i)
print('List after removing duplicates: ',result)

--------------------------------------------------------------------------------------
4. Write a Python program to check if a list is sorted in ascending order.

List = list(map(int,input('Enter a number by space separated: ').split()))
print(List)
if sorted(List) ==  List:
    print('List is sorted in ascending order')
else:
    print('List is not sorted in ascending order')

----------------------------------------------------------------------------------------
5. Write a Python program to find the second largest element in a list.

List = list(map(int,input('Enter a number by space separated: ').split()))
print(List)
List = sorted(List)
print('Second largest element in a list:  ',List[-2])

-----------------------------------------------------------------------------------------
6. Write a Python program to sort a list of strings in alphabetical order.

List = list(input('Enter a str by space separated: ').split())
print(List)
List.sort()
print('Updated list: ',List)
-----------------------------------------------------------------------------------------
7. Write a Python program to find the common elements between two lists.

def common_element(List1,List2):
    result = [i for i in List1 if i in List2 ]
    return result

List1 = list(map(int,input('Enter a number by space separated: ').split()))
print(List1)
List2 = list(map(int,input('Enter a number by space separated: ').split()))
print(List2)
print('common elements between two lists: ',common_element(List1,List2))

----------------------------------------------------------------------------------
8. Write a Python program to remove the nth occurrence of an element from a list.

def remove_element(List):
    List.pop(index)

List = list(map(int,input('Enter a number by space separated: ').split()))
print(List)
index = int(input('Enter a index number you want to remove: '))
remove_element(List)
print('updated list: ',List)

----------------------------------------------------------------------------------
9. Write a Python program to find the difference between two lists.

def diff_list(List1,List2):
    diff_result = list(set(List1).symmetric_difference(List2))
    print('difference between two lists: ',diff_result)

List1 = list(map(int,input('Enter a number by space separated: ').split()))
print(List1)
List2 = list(map(int,input('Enter a number by space separated: ').split()))
print(List2)
diff_list(List1,List2)

-------------------------------------------------------------------------------------
10. Write a Python program to remove the elements of a list that are divisible by 3.


def remove(List):
    result = []
    for i in List:
        if i % 3 != 0:
            result.append(i)
    return result

List = list(map(int,input('Enter a number by space separated: ').split()))
print(List)
print('List after removing the elements that are divisible by 3 : ',remove(List))

------------------------------------------------------------------------------------
"""



