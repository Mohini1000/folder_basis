# Take different index one after other string

s1 = 'RAVI' # 4
s2 = 'TEJA' # 4
i, j = 0, 0
output = ''
while i < len(s1) or j < len(s2):
    output = output + s1[i] + s2[j]  # after first string len end it will give null and we cant concat null to the string
    i = i + 1                   # if both string have same length then we can use this code
    j = j + 1
print(output)


# this is when strings having different sizes
s1 = "Raja"  # len  = 4
s2 = "Chaitanya"  # len =9
i, j = 0, 0
output = ""
while i < len(s1) or j < len(s2):
    if i < len(s1):
        output = output + s1[i]
        i = i + 1
    if j < len(s2):
        output = output + s2[j]
        j = j + 1
print(output)

#-------------------------------------------------------------------------------------------

# assume input string contain alphabet and digits
# wap to sort character of string ,first alphabet by digits
# Output:
# ABD134

ip = "B4A1D3"
alpha = ""
digit = ""

for element in ip:
    if element.isalpha()==True:
        alpha += element

    if element.isdigit() == True:
        digit += str(element)

print(alpha)
print(digit)

sorted_alpha_list = sorted(alpha)
sorted_alpha_string = "".join(sorted_alpha_list)
print(sorted_alpha_string)

sorted_digit_list = sorted(digit)
sorted_digit_string = "".join(sorted_digit_list)
print(sorted_digit_string)

print(sorted_alpha_string+sorted_digit_string)

#-------------------------------------------------------------------------------------------

'''
2)
input:
a4b3c2
output:
aaaabbbcc'''

ip = 'a4b3c2'
output = ""
for char in ip:  # a4b3c2
    if char.isalpha():
        x = char  # a b c
    else:
        digit = int(char) #4
        output = output + x * digit
print(output)

#-------------------------------------------------------------------------------------------

'''
3)
input:
aaaabbbbxxz 
output:
a4b2c1z1'''

s = "aaaabbbbxxz"
newstr = ""
count = 1
for i in range(1, len(s)):  # it starts from 1 because to check index of previous one
    if s[i] == s[i - 1]:
        count = count + 1
    else:  # when if stops counting it will return the element in string
        newstr += str(count) + s[i - 1]
        count = 1  # and again start count from 1 for next element

newstr += str(count) + s[i - 1]
print(newstr)

'''
3)
input:
aaaabbbbxxz
output:
4ab2c1z'''

input = 'aaaabbbbxxzz'

len = int(len(input))
c = 0
b = ''
i = 0
while c < len:
    if input[i] == input[c]:
        c = c + 1
    else:
        b = b + (input[i] + str(c - i))
        i = c
b = b + (input[i] + str(c - i))
print(b)

#-------------------------------------------------------------------------------------------
# by using while loop:  from chatgpt
input_string = "aaaabbbbxxz"

# Initialize variables to store the previous character and its count
prev_char = input_string[0]
count = 1

# Initialize an empty string to store the output
output = ""

# Start iterating from the second character
index = 1
while index < len(input_string):
    char = input_string[index]
    if char == prev_char:
        count += 1
    else:
        output += str(count) + prev_char
        count = 1    # again set counter 1
        prev_char = char
    index += 1    # this increase the index

# Add the count of the last character and its character to the output
output += str(count) + prev_char
print(output)
#-----------------------------------------------------------------------------------------

# Input string
input_string = "aaaabbbbxxz"
# Compress the string
output_string = compress_string(input_string)
# Print the compressed string
print(output_string)

'''
4)
input:
a4k3b2

output:
aeknbd'''

s = 'a4k3b2'
output = ''
for char in s:
    if char.isalpha():
        x = char
        output = output + char
    else:
        d = int(char)
        newchar = chr(ord(x) + d)
        output = output + newchar
print(output)




char = "c"  # unicode starts form 97 = a
print(ord(char))  # ord gives us unicode of this number
newchar = chr(100)  # chr gives unicode to letter
print(newchar)


#1)remove duplicate charcter's from the given string:

S='AAAAAAAAAAAAAZZZZZZZZZCCCCCCCCFFFFFFFFFGGGGHHH'
s="AZCGH"

set1 =(set(S))
for i in set1:
    print(i,end="")


S='AAAAAAAAAAAAAZZZZZZZZZCCCCCCCCFFFFFFFFFGGGGHHH'
s="AZCGH"
str =""
for i in range(0, len(S)):
    if S[i] not in str:
        str+= S[i]
    else:
        continue

print(str)


# --------------------------------------------------------------------------
'''2)take input from cx and find how many vowels present in the given strings

output:
a ocuurs 2 times
E ocuurns 4 times'''

s = input("enter the string:")
v = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
d = {}
for char in s:
    if char in v:
        d[char] = d.get(char, 0) + 1 # 0 is for default value means if letter not present in v
        print(d)                     #then replace as 0, if letter present add 1 in it.
for k, v in sorted(d.items()):
    print(k,v)


    print('{} occurs {} times'.format(k, v))

# -----------------------------------------------------------------------------

'''Assume input strings contain alphabets and digits.
wap to sort character of the string, first alphabets followed by digits

Input:
B4A1D3
Output:
ABD134'''

input = "B4A1D3"
str = ""
str1 = ""

num = len(input)
for i in range(num):
    if input[i].isalpha() == True:
        str = str + input[i]
    if input[i].isdigit() == True:
        str1 = str1 + input[i]

sorting = ''.join(sorted(str)) + ''.join(sorted(str1))  # here join used to join the strings elements in single string with sorted function
print(sorting)


#----------------------------------------------------------------

str = "chait"
sorted = sorted(str)  # sorted gives list with sorting character int the string
print(sorted)

str = "chait"
sorted1 = "".join(sorted(str))
print(sorted1)

# ================================ Join ========================================
# use of join in the python
''' join is the used for joining the element in list,strings and tuple into a single string'''

# Joining elements of a list into a string
my_list = ['Hello', 'world', '!']
result = ' '.join(my_list)
print(result)  # Output: Hello world !

# Joining elements of a tuple into a string
my_tuple = ('Python', 'is', 'awesome')
result = '-'.join(my_tuple)
print(result)  # Output: Python-is-awesome

# Joining characters of a string into a string
my_string = 'Hello'
result = ':'.join(my_string)
print(result)  # Output: H:e:l:l:o

# ================================== ord() and chr() ==================================
'''ord() - converts a character into the unicode
and chr() - converts the unicode into the char'''

# Define a string
text = "Hello"
lst = []
for words in text:
    lst.append(ord(words))
print(lst)

for elements in lst:
    elements = chr(elements)
    print(elements, end="")

# same using list comprehensssions
text = "Hello"
# Convert each character to its Unicode code point using ord()
code_points = [ord(char) for char in text]
print("Unicode code points:", code_points)

# Convert each Unicode code point back to characters using chr()
characters = [chr(code) for code in code_points]
print("Characters:", ''.join(characters))  # here convert list element in the string using join function

# ============================== sorted() ============================

'''sorted() function is used to return a new sorted list from the elements of any iterable 
(like lists, tuples, dictionaries, and more). The sorting is done in ascending order by default,
 but you can specify the reverse=True parameter to sort in descending order. 
 Additionally, you can use the key parameter to specify a function to be called on each element 
 prior to making comparisons.'''

# imp: for strings,list, tuple and dictionaries only

# Sorting a list of numbers in ascending order
numbers = [3, 1, 4, 1, 5, 9, 2]
print(sorted(numbers))

# Sorting a list of numbers in descending order
print(sorted(numbers, reverse=True))

# Sorting a list of strings based on their lengths
words = ['banana', 'pie', 'Washington', 'book']
print(sorted(words, key=len))

# Sorting a dictionary by its values
data = {'apple': 10, 'orange': 5, 'banana': 15}
sorted_data = sorted(data.items(), key=lambda x: x[1])
print(sorted_data)  # This will print a list of tuples sorted by the dictionary's values

# Sorting a dictionary by its keys
data = {'apple': 10, 'orange': 5, 'banana': 15}
sorted_data = sorted(data.items())
print(sorted_data)  # This will print a list of tuples sorted by the dictionary's keys

'''Important Notes
sorted() always returns a new list containing all the elements of the input sorted, 
unlike the .sort() method of lists, which modifies the list in place and returns None.
The key function transforms each element before sorting. 
The sorting happens based on its return value, not directly on the elements themselves.
The sorted() function works on any iterable,
 not just lists, making it a versatile option for various data types'''

# sorted in tuple
my_tuple = (3, 1, 2, 5, 4)
sorted_tuple = tuple(sorted(my_tuple))  # typecast list into tuple

print(sorted_tuple)  # Output: (1, 2, 3, 4, 5)

# if we want to use the sorting for string syntax is like this
# Sorting characters of a string alphabetically
my_string = "yzk"
sorted_string = ''.join(sorted(my_string))
print(sorted_string)  # Output: 'ehllo'

# Sorting characters of a string in reverse order
reverse_sorted_string = ''.join(sorted(my_string, reverse=True))
print(reverse_sorted_string)  # Output: 'ollhe'

# ================================ get() in dictionaries ===============================
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Retrieving value for an existing key
value1 = my_dict.get('a')
print(value1)  # Output: 1

# Retrieving value for a non-existing key
value2 = my_dict.get('d')
print(value2)  # Output: None

# Retrieving value for a non-existing key with a default value
value3 = my_dict.get('d', "hey")
print(value3)  # Output: 0

# ========================================================================================
# count the number of time string element
counter =1
inp = "aaaabbbbxxzzz"
output = ""                  #a4b4x2

for index in range(1,len(inp)):
    if inp[index] == inp[index-1]:
        counter+=1
    else:
        output = output + inp[index-1] + str(counter)
        counter =1

output += inp[-1] + str(counter) # this is for last grp
print(output)

'''
aaaa 0-1-2-3
bbbb 4-5-6-7
xx 8-9
zzz -10 11 12'''

#----------------------Filter in python----------------------------------------------
# Define a function to filter even numbers
def is_even(num):
    return num % 2 == 0

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter() to filter even numbers from the list
even_numbers = filter(is_even, numbers)

# Convert the filter object to a list (or any other iterable)
even_numbers_list = list(even_numbers)

# Print the result
print(even_numbers_list)  # Output: [2, 4, 6, 8, 10]
#---------------------OR-------------------------------
def even(num):
    for x in number:
        if x % 2==0:
            print("even number is",x)


number=[2,3,4,6,7,8,9]
even(number)

#--------------------------------------------------------------------
#give name and mark data in dict form
n=int(input("enter no of student="))
dict={}
for x in range(n):
    name=input("enter name of student {}=".format(x+1))
    marks=input("enter % mark of student=")
    dict[name]=marks
print(dict)


#----------------------------------------------------
#wap to take dictionary from keyboard and print sum of values

dict={}
n=int(input("enter no of keys="))
for x in range(n):
    key=input("enter the keys=")
    values=int(input("enter the values="))
    dict[key]=values
print(dict)
val=0
for i in dict.values():
    val=val+i
print("sum of values is",val)

#----------------------------------------------------
#give string, count no of occurance of letter

string="learning python is difficult"
for x in range(len(string)):
    cnt=string.count(string[x])
    print(f"no of occurence of {string[x]} is {cnt} times")


