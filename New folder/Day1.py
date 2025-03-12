# Stings are immutable
# we cant change the string by assigning value using slicing
a = 'Hello'
a[1]= 'Z'# can't change



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
# if we add two strings by , then there will be a single space between them
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

# str can handle arithmatic operation
total_pancakes = 10
pancakes_eaten = 5
print("Only " + str(total_pancakes - pancakes_eaten) + " pancakes left.")

# F String and string interpolation
name  = "tiger"
head  = 1
leg = 4
print(name + " has "+ str(head)+ " head and "+ str(leg) + ' legs') # string interpolation

print(f"{name} has {head} head and {leg} legs and their total organs are {head*leg}") # f string

phrase = "the surprise is in here somewhere"
print(phrase.find("surprise"))
print(phrase.find("r"))
