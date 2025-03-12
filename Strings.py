# Stings are immutable
# we cant change the string by assigning value using slicing
a = 'Hello'
a[1]= 'Z'

----------------------------------------------------------------------------------------
print('hello python')
print(5)
print(True)
print(4+5)
print('4+5')
print('4>5',4>5)
print('4>5'+' '+ str(4>5))
print('this is string' +' ' + str(10))
# print('hello')
'''print('hello')'''

greeting = "Hello, World"
print(greeting)
----------------------------------------------------------------------------------------
a = 'chaitanya'
print(type(a))
print(len(a))  # count starts with 1
print(a[0])
print(a[0:4]) # upper index always upper index-1   --- 0 to 3
print(a[0:])
print(a[0::3])
print(a[0:3:2])
print(a[::])
print(a[::-1]) #this is for reverse string

----------------------------------------------------------------------------------------
paragraph = 'This planet has—or rather had—a problem, which was \
this: most of the people living on it were unhappy for pretty much \
of the time. Many solutions were suggested for this problem, but \
most of these were largely concerned with the movements of small \
green pieces of paper, which is odd because on the whole it wasn \
the small green pieces of paper that were unhappy.'
print(paragraph) # here \ is required for nextline
# all string printed in one line only

msg = ('hello Good morning\
 this is the python session')
print(msg)


paragraph = """This planet has—or rather had—a problem, which was
this: most of the people living on it were unhappy for pretty much
of the time. Many solutions were suggested for this problem, but
most of these were largely concerned with the movements of small
green pieces of paper, which is odd because on the whole it wasn't
the small green pieces of paper that were unhappy."""
print(paragraph)  # in the tripple quote as it is string printed
# no \ required for the next line


x = 'This is pycharm code'
print(x.startswith('Thi'))
print(x.startswith('c'))
print(x.endswith('e'))

# --------------------input-------------------------------------
var = input("Enter your name here: ")
print(var)
print(type(var))

num1 = int(input("put num1 here: "))
num2 = input("put num2 here: ")
addition = (num1) + int(num2)
print(addition)


num = "2"
print(num + num,num)
# if we add two stings by + then there will no space between those two strings
# if we add two strings by , then theere will be a single space between them
print(num*100)

print("3" + 3)  # for addtion of string using + , there is need of same datatype
print('3',3)   # for addition with , there is no need of same datatype

new_num = float(num)
print(float(num))
print(int(new_num))

num1 = ('10.5')
print(float(num1))
print(int(num1))  # we cant convert the float in the string  form to the integer

num_pancakes = 10
print("I am going to eat " + str(num_pancakes) + " pancakes.")
print("I am going to eat " , num_pancakes , " pancakes.")
----------------------------------------------------------------------------------------
# str can handle arithmatic operation
total_pancakes = 10
pancakes_eaten = 5
print("Only " + str(total_pancakes - pancakes_eaten) + " pancakes left.")
----------------------------------------------------------------------------------------
# F String and string interpolation
name  = "tiger"
head  = 1
leg = 4
print(name + " has "+ str(head)+ " head and "+ str(leg) + ' legs') # string interpolation

print(f"{name} has {head} head and {leg} legs and their total organs are {head*leg}") # f string

phrase = "the surprise is in here somewhere"
print(phrase.find("surprise"))
print(phrase.find("r"))
----------------------------------------------------------------------------------------
# extracting all words on by one
word = 'Hello how are you'
for words in word:
    print(words)

txt = "The best things in life are free!"
print("free" in txt)  # in opeerator check

txt = "The best things in life are free!"
if "india" in txt:
  print("Yes, 'free' is present.")
else:
    print('given text is not present')

txt = "The best things in life are free!"
print("expensive" not in txt)

b = "Hello, World!"
print(b[-5:-2])   # -2 -1  = -3

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.replace("H", "J"))
print(a.replace('Hello', 'Hey'))

a = "Hello, World!,hey, good morning"
print(a.split(","))

aa = 'india. is. best. contry'
print(aa.split("."))

lst = [1,2,3,4,'chaitanya',True, False,4555.565]
print(type(lst))


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

print(f"My name is john , and i am {age}")


txt = "We are the so-called \"Vikings\" from the north."  # here \" is the escape character
print(txt)

txt = "We are the so-called \"Vikings\" from the north."  # here \" is the escape character
txt1 ="We are the so-called \'Vikings\' from the north."
txt2 ="We are the \r so-called \\Vikings\\ from the  \n north."
txt3 = "hello \t how are\b you "
print(txt3)
print(txt)
print(txt1)
print(txt2)

# Strings methods
# capitalize
str = 'age 50 is my AGE '
print(str)
x = str.capitalize()  # change first character capital and rest converted into lower case
print(x)
#-----------------------------
# casefold - convert text into lower case
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)
#---------------------------------
# Returned centered string
txt = 'apple'
x = txt.center(20,' ') # by default filling char is space
print(x)

txt = "Apple"
x = txt.center(20, "O")   # apple will be start at center i.e starts from 10
print(x)
#------------
# Count
# syntax : string.count(value, start, end)
text = "I love apples, apple are my favorite fruit"
x = text.count("apple")  # it will give how much time specific string occure in the string
print(x)

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)
#---------------
#ExpandTabs
txt = "H\te\tl\tl\to"
x = txt.expandtabs(5)
print(x)
#--------------------
#Find -- gives index of string starts with 0
txt = 'hello good morning'
y = txt.find('x')
z = txt.index ('h')
x = txt.find('mor',0,5)
print(y)
print(z)
print(x)
#syntax :string.find(value, start, end)
'''If the value is not found, the find() method returns -1, but the index() method will raise an exception:'''
----------------------------------------------------------------------------------------
#Format
txt = "For only {price:.4f} dollars!"  # 4f indicate 4 digits
print(txt.format(price = 49))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)   # here use indexing
txt3 = "My name is {}, I'm {}".format("John",36)  # we can take blanks also
print(txt1,txt2,txt3)
----------------------------------------------------------------------------------------
# isalnum
txt = '1Name56'
x = txt.isalnum()  # check alphabets with numeric
print(x)
y = txt.isalpha()  #check only aphabets
print(y)

txt = "Company123"
x = txt.isascii()
print(x)

txt = "1234"
x = txt.isdecimal()
print(x)

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a.isdecimal())
print(b.isdecimal())

----------------------------------------------------------------------------------------
# isdigit
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print(a.isdigit())
print(b.isdigit())

txt = "50800"
x = txt.isdigit()
print(x)
----------------------------------------------------------------------------------------
# isidentifier  -- valid identifier contains underscore,numericals
txt = '_Chaitanya_Nagare05'
txt1 = '2_Chaitanya_Nagare05'
a = txt.isidentifier()
b = txt1.isidentifier()
print(a)
print(b)

----------------------------------------------------------------------------------------
# islower- check wheather all charcter are lower or not
txt = 'heello World'
a = txt.islower()
print(a)
----------------------------------------------------------------------------------------
# isnumeric -- this will check the numeric inside the strings
a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"
f = '5555'
print(a.isnumeric()) # true
print(b.isnumeric()) # true
print(c.isnumeric()) # false
print(d.isnumeric()) # false
print(e.isnumeric()) # false
print(f.isnumeric()) # true
----------------------------------------------------------------------------------------
# isprintable
txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)
----------------------------------------------------------------------------------------
# isspace
txt = "   s   "
x = txt.isspace()
print(x)
----------------------------------------------------------------------------------------
# istitle - check all letter first name is capital or not
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)

a = "HELLO, AND WELCOME TO MY WORLD"  # this is not fit in istitle
b = "Hello"
c = "22 Names"  # this is also title
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())

# issuper  - check wheather all are capital or not
a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print(a.isupper())
print(b.isupper())
print(c.isupper())
----------------------------------------------------------------------------------------
# join
'''tupple joining'''
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

'''Dictionary keys joining'''
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)  #it joins all keys

'''list elements joining'''
lst = ['chaitanya', 'nagare','5', '69' ,'True'] # we cant join bool values and integer by join
seperator = ' and '
x = seperator.join(lst)
print(x)
----------------------------------------------------------------------------------------
# ljust --Return a 20 characters long, left justified version of the word "banana":
txt = "apple"
x = txt.ljust(10)   # 10 including apple text
print(x, "is my favorite fruit.")

txt = "banana"
x = txt.ljust(10, "5")
print(x)

#lower, lstrip, rstrip, strip, upper
----------------------------------------------------------------------------------------
#makestrans -- method to replace any "S" characters with a "P" character:
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)  # to replace multiple charactter
print(txt.translate(mytable))  # translate() method to replace any "S" characters with a "P" character:

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))
# third parameter in the mapping table describes characters that you want to remove from the string:

#translate() method to replace any "S" characters with a "P" character:

----------------------------------------------------------------------------------------
# partition --search a word and returns into the tuple
txt = "I could eat apple all day"
x = txt.partition("apple")
print(x)

txt = "I could eat bananas all day"
x = txt.partition("apples")
print(x)
'''If the specified value is not found, the partition() method returns a tuple containing: 
1 - the whole string, 
2 - an empty string, 
3 - an empty string:'''
----------------------------------------------------------------------------------------
# replace
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
'''syntax:  string.replace(oldvalue, newvalue, count)'''

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)
-------------------------------------------------------------------------------
# rfind
txt = "Mi casa, su casa."
x = txt.rfind("casa",0,5)
print(x)

txt = "Hello, welcome to my world."
print(txt.rfind("world",6,50))
print(txt.rindex("e"))
# The rfind() method is almost the same as the rindex() method-
------------------------------------------------------------------------------------------
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("all")
print(x)
'''Search for the last occurrence of the word "bananas", and return a tuple with three elements:

1 - everything before the "match"
2 - the "match"
3 - everything after the "match"'''
----------------------------------------------------------------------------------------
# rsplit - Split a string into a list, using comma, followed by a space (, ) as the separator:
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

txt = "welcome to the jungle"
x = txt.split()
print(x)


txt = "apple, banana, cherry"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)
print(x)


---------------------------------------------------------
sentence = "Hello, how are you today ?"
print(sentence.split())
# Output: ['Hello,', 'how', 'are', 'you', 'today?']

print(sentence.rsplit())
# Output: ['Hello,', 'how', 'are', 'you', 'today?']

print(sentence.split(maxsplit=2))
# Output: ['Hello,', 'how are you today?']

print(sentence.rsplit(maxsplit=2))
# Output: ['Hello, how are you', 'today?']

----------------------------------------------------------------
# rstrip --Remove the trailing characters if they are commas, periods, s, q, or w:
txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")
print(x)

txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")
----------------------------------------------------------------
# Splitlines--Split a string into a list where each line is a list item:
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines(True)
print(x)
----------------------------------------------------------------

#Swapcase -It swipe the case
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

----------------------------------------------------------------

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))
----------------------------------------------------------------
# Zfill
#Fill the string with zeros until it is 10 characters long:
txt = "50"
x = txt.zfill(10)
print(x)