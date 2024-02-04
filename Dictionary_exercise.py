"""
Dictionary Exercises:
1. Write a Python program to iterate over a dictionary and print its keys and values.

d = {1:'A',2:'B',3:'C'}
print(d)
print('Keys of dictionary: ',d.keys())
print('Values of dictionary: ',d.values())

===========================================================================================
2. Write a Python program to check if a key exists in a dictionary.

d = {1:'A',2:'B',3:'C'}
print(d)
n = int(input('Enter a key you want to check: '))
if n in d.keys():
    print('key exists in a dictionary')
else:
    print('key is not exists in a dictionary')

================================================================================================
3. Write a Python program to get the value associated with a key in a dictionary.

dict1 = {i:i*i for i in range(1,11)}
print('Keys present in dictionary: ', list(dict1.keys()))
x = int(input('Enter a key to get value associated: '))
print('value associated with a given key : ',dict1[x])


===================================================================================================
4. Write a Python program to remove a key from a dictionary.

dict1 = {i:i*i for i in range(1,11)}
print(dict1)
x = int(input('Enter a key to remove: '))
dict1.pop(x)
print('Updated dictionary: ',dict1)

===================================================================================================
5. Write a Python program to sort a dictionary by its values.

dict1 = {i:i*i for i in range(1,11)}
dict2 = dict(sorted(dict1.items(), key=lambda item: item[1]))
print(dict2)

===================================================================================================
6. Write a Python program to merge two dictionaries.

dict1 = {5:'Mum',6:'puna',7:'satara'}
dict2 =  {1:'A',2:'B',3:'C'}
dict2.update(dict1.items())
print(dict2)

===================================================================================================
7. Write a Python program to count the frequency of each element in a dictionary.

def count_frequency(input_dict):
    frequency_dict = {}  # Dictionary to store element frequencies
    for key, value in input_dict.items():
        if value in frequency_dict:
            frequency_dict[value] += 1
        else:
            frequency_dict[value] = 1
    return frequency_dict

input_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 1}
frequency_result = count_frequency(input_dict)

print("Frequency of each element:")
for key, value in frequency_result.items():
    print(f"'{key}': {value}")

====================================================================================================
8. Write a Python program to find the length of a dictionary.

dict1 = {5:'Mum',6:'puna',7:'satara'}
print(dict1)
print('Length of dictionary: ',len(dict1))

===================================================================================================
9. Write a Python program to check if a dictionary is empty.

dict1 = {5:'Mum',6:'puna',7:'satara'}
dict2 = {}
print('Dictionary is empty' if len(dict1) == 0 else 'Dictionary is not empty')
print('Dictionary is empty' if len(dict2) == 0 else 'Dictionary is not empty')

===================================================================================================
10. Write a Python program to find the keys with the maximum and minimum values in a dictionary.


dict1 = {i:i*i for i in range(5,48)}
print(dict1)
max_d = [k for k in dict1 if dict1[k] == max(dict1.values())]
min_d = [k for k in dict1 if dict1[k] == min(dict1.values())]
print('Key having max value is: ',*max_d)
print('Key having min value is: ',*min_d)

========================================================================================================

"""
