"""

1. Write a Python program to count the number of characters in a string.

def count_char(s):
    return len(s)

s = input('Enter a string: ')
print("Number of characters in a string : ",count_char(s))

-------------------------------------------------------------------------------------
2. Write a Python program to reverse a string.

def reverse_str(s):
    return s[::-1]
s = input('Enter a string: ')
print("Reverse of a string is : ",reverse_str(s))

--------------------------------------------------------------------------------------
3. Write a Python program to check if a string is a palindrome.

def palindrome_str(s):
    if s == s[::-1]:
        print('This string is a palindrome')
    else:
        print('This string is not a palindrome')

s = input('Enter a string: ')
(palindrome_str(s))

------------------------------------------------------------------------------------------
4. Write a Python program to remove all the vowels from a string.

def remove_vowel(s):
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    result = ' '
    for char in s:
        if char not in vowels:
            result += char
    return result

s = input('Enter a string: ')
print("After removing all vowels :",remove_vowel(s))

----------------------------------------------------------------------------------------
5. Write a Python program to find the first non-repeating character in a string.

def non_repeating_character(s):
    s = s.lower()
    temp = [i for i in s if s.count(i)==1]
    return temp[0] if temp else -1

s = input('Enter a string: ')
print("First non-repeating character in a string:" ,non_repeating_character(s))

---------------------------------------------------------------------------------------
6. Write a Python program to capitalize the first letter of each word in a string.

def cap_first_letter(s):
    return s.title()

s = input('Enter a string: ')
print(cap_first_letter(s))

------------------------------------------------------------------------------
7. Write a Python program to check if a string is an anagram of another string.

def anagram(s1,s2):
    if (sorted(s1.lower())==sorted(s2.lower())):
        print('String is an anagram of another string.')
    else:
        print('String is not an anagram of another string.')

s1 = input('Enter a string: ')
s2 = input('Enter a string: ')

(anagram(s1,s2))

----------------------------------------------------------------------------------
8. Write a Python program to find the most frequent character in a string.

x = input('Enter a string: ')
d = { }
for i in x:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)
print('Most frequent character is : ',max(d,key=d.get))

---------------------------------------------------------------------------------
9. Write a Python program to check if a string is a valid email address.

import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def check(email):

    if (re.fullmatch(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")

email = input('Enter  mail id: ')
(check(email))

------------------------------------------------------------------------------------
10. Write a Python program to find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s):
    maxLen = 1
    if s == '':
        return 0
    for i in range(len(s)):
        substring = s[i]
        for j in range(i + 1, len(s)):
            if s[
                j] not in substring:
                substring = substring + s[j]
                maxLen = max(maxLen, len(substring))
            else:
                break
    return maxLen

s = input('Enter a string: ')
print("length  of longest substring: ",lengthOfLongestSubstring(s))

--------------------------------------------------------------------------------
"""


