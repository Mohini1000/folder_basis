lst = ['Chaitanya',52,True,False,25.00]
print(lst)
print(type(lst))
print(lst[0]) # slicing always counts from 0
print(lst[0:3])
print(lst[0::2])
print(len(lst)) # len always count from 1

strings = ('Chaitanya',52,True,False,25.00)
print(type(strings))

lst = list(strings)
print(lst)
print(type(lst))

---------------------------------------
# To change the elements inside the list

lst = ['Chaitanya',52,True,False,25.00]
lst[2:4]  = [100,200]
print(lst)
lst[2:4]  = [500]
print(lst)

# insert
lst = ['Chaitanya',52,True,False,25.00]
lst.insert(2,("india","Hello"))
print(lst)

# append
lst = ['Chaitanya',52,True,False,25.00]
 print(lst)
 lst.append("India")
 print(lst)

 lst.append(["Pune",'Goa',"Mumbai"]) # in append we can add only one argument
print(lst)

 # extend
 tup = (["Pune",'Goa',"Mumbai"])
lst.extend(tup)
print(lst)

#----------------------------------------------------------------
# To remove the elements from the list
lst = ['Chaitanya',52,True,False,25.00]
lst.remove(True)
print(lst)

lst = ['Chaitanya',52,True,False,25.00]
lst[2:4]  = []
print(lst)

lst = ['Chaitanya',52,True,False,25.00]
lst.pop()
print(lst) # pop will delete lst element of the list if we not provide any indexing


lst = ['Chaitanya',52,True,False,25.00]
lst.pop(0)
print(lst)

lst.pop([0:3])   # this is not allowed

#Clear
lst = ['Chaitanya',52,True,False,25.00]
lst.clear()
print(lst)

# del
lst = ['Chaitanya',52,True,False,25.00]
del lst
print(lst)


# loop inside the list
lst = ['Chaitanya',52,True,False,25.00]

# for loop
for x in range(100):
 print("The product is", x * 2)

lst = ['Chaitanya',52,True,False,25.00]
for x in range(5):
 print(lst[x])

for x in range(len(lst)):
 print(lst[x])  # slicing
#------------------------------------------------
 lst = ['Chaitanya', 52, True, False, 25.00]
 for elements in lst:
  print(elements)

  lst = ['Chaitanya', 52, True, False, 25.00]
 [print(elements) for elements in lst]    # list comprehession
#------------------------------------------------

for x in range(len(lst)):
 print(lst[x] ,"having index is ",x)

for i in range(0,101,2):
 print(i)

# convert range function into the list
a = list(range(0,15))
print(a)
print(type(a))

for i in a:
 print(a)


# list comprehenssion
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Syntax
#newlist = [expression for item in iterable if condition == True]

# assign new value to the entire list
newlist = ['hello' for x in fruits]


# list comprehenssion with for loop and print statement with if else condition
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

for x in fruits:
 if x != "banana":
  print(x)
 else:
  print('orange')

new_list = [x if x != "banana" else "orange" for x in fruits]
print(new_list)

# sorting list
thislist = [ True ,False ,25,25.0]
thislist.sort()  # this equal to thislist.sort(reverse = False)
print(thislist)

# to reverse the list
thislist.sort(reverse= True)
print(thislist)

'''In Python, data types can be categorized into primitive (or built-in) data types and non-primitive (or complex) data types. Here's a brief overview of each:

1. Primitive (or Built-in) Data Types:
   - `int`: Integer numbers without decimal points.
   - `float`: Floating-point numbers, which include decimal points.
   - `bool`: Boolean values, `True` or `False`.
   - `NoneType`: The type of the `None` object, which represents absence of a value or a null value.

2. Non-Primitive (or Complex) Data Types:
   - `str`: Strings, sequences of characters enclosed in single or double quotes.
   - `list`: Ordered collection of items. Mutable.
   - `tuple`: Ordered collection of items. Immutable.
   - `set`: Unordered collection of unique items. Mutable.
   - `dict`: Collection of key-value pairs. Mutable.

Primitive data types are considered fundamental and are built into the Python language itself,
 while non-primitive data types are built upon these primitives and provide more complex data
  structures and functionalities.'''

'''boolean: The default value is false.
false 0
true 1
int: The default value is 0.
float: The default value is 0.0.'''


#sorting with cases- Sentence case sort first then lower cases
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# reverse -
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

'''notes:
In the reverse it will reverse with the indexes
and In the sort it will sort with alphabets
Sentence case sort first then lower cases
'''

# copy and list method used to make a duplicate list from existing once
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


# joining the list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# joining with append function
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

# joining lists with extend method
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

