
# link : https://www.w3schools.com/python/python_functions.asp

def add(num1,num2):  # parameterise function
    sum = num1+num2
    return sum*2
    # print(f"The sum of num1 and num2 is {sum}")

add(10,20)
add("Chaitanya"," Nagare")
add(True ,False)

def number(n):
    print("square is",n*n)
number(2)
#*********** function with lambda ***************

#using function
def addition(n):
    return n+n
numbers=(1,2,3,4)
result=map(addition,numbers) #here we 1st mention function name then (list,tuple name)
print(list(result))

#using lambda

numbers=(2,4,6,8)
result=map(lambda x:x+x,numbers)  #here first lambda then ,(list,tuple name)
print(list(result))

#add two list using func

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

def addition(numbers1,numbers2):
    return numbers1+numbers2
result=map(addition,numbers1,numbers2)
print(list(result))

#using lambda
numbers1 = [2, 4, 6]
numbers2 = [4, 5, 6]
result=map(lambda x,y:x+y,numbers1,numbers2)
print(list(result))

#3)given is list if numbers is even double it if odd remains same

lst=[2,3,4,6,7,8,9]
def odd_even(n):
    if n%2==0:
        return n*2
    else:
        return n
result=map(odd_even,lst)
print(list(result))

#using lambda
lst=[2,3,4,6,7,8,9]
result=map(lambda x:x*2 if x%2==0 else x,lst)
print(list(result))


#4)cube of list
org_list = [1, 2, 3, 4, 5]
def cube(n):
    return n**3
result=map(cube,org_list) #here we have to mention function name first then list name
print(list(result))

#using lambda
org_list = [1, 3, 6, 9, 5]
result=map(lambda x:x**3,org_list)
print(list(result))

#5)to find factorial

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
factorial(4)


#******************chaitanya questions**************
#1) for i in list:
#    print(i)

lst=[10,20,"mahi","priya"]
result=map(lambda x:[x for x in lst],lst)
print(list(result))

#2)for i in list:
# if i <10:
# print("Greater")

lst=[10,50,70,6,2,100,80]
result=map(lambda x:print("greater")if x>10 else print("smaller"),lst )
print(list(result))

#3)
# for i in list:
# if i >10:
# print("greater")
# else:
# print("Smaller")

lst=[10,50,70,6,2,100,80]
result=map(lambda x:["greater" if x>10 else "smaller" for x in lst],lst)
print(tuple(result))

#4)


#*******************************************************************************
#to get list of fruits which starts with a
def start_with_a(s):
    return s[0]=="a"
fruits=["apple","banana","angle","cherry","amar","aarti"]
result=filter(start_with_a,fruits) #if we use map it give result for all element as true or false
print(list(result))

#using lambda
fruits=["apple","banana","angle","cherry","amar","aarti"]
result=filter(lambda x: x[0]=="a",fruits)
print(list(result))


#to get odd_even

def odd_even(n):
    return n%2==0
lst=[2,3,4,5,6,7,8,9]
result=filter(odd_even,lst)
print(list(result))



lst=[2,3,4,5,6,7,8,9]
result=filter(lambda x:x%2==0,lst)
print(list(result))



#addition of element in list using function and lambda

from functools import reduce
def add(n1,n2):
    return n1+n2
lst=[2,3,4,5,6,7,8,9] #here reduce did add of 2 element every time so we take 2 argument n1,n2
result=reduce(add,lst)
print(result)        #it give single output so we can not give print(list(result))


from functools import reduce
lst=[2,3,4,5,6,7,8,9]
result=reduce(lambda x,y:x+y,lst)
print(result)

#---------------------------------------------------------
#all map, filter and reduce in one code
# even,double,sum
from functools import reduce

lst=[2,3,4,5,6,7,8,9]

result=map(lambda x:x*2,lst)
# print(list(result))

result1=map(lambda x: x%2==0,result)
# print(list(result1))

result2=reduce(lambda x,y:x+y,result)
print(result2)

#---------------------------------------------------------


#----------------------------------------------------
# parameterless function
def sentence():
    print("this is the sentence function")

sentence()




# args - here function calling parameters are in the tuple
'''If you do not know how many arguments that will be passed into your function, 
add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:'''
def information(*kids):
    # print(f"My name is {kids[2]}")
    for names in kids:
        print(names)

information("chaitanya","Rajesh","Shivraj","vishal")

# if we add two asterisk: ** before the parameter name in the function definition, it work likes dictionary
# kwargs - here function calling parameter are in the dictionary
def student_Data(**dict):
    for key,values in dict.items():
        print(f"The {key} is {values}")

student_Data(Name = "chaitanya",Address = "Pune",Age = 26)


# default parameter
def my_info(country = "India"):
    print(f"My country name is {country} ")


my_info("US")
my_info("China")
my_info()  # here it will take default value



# passing list as a argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
print('\n')
my_function(["apple", "banana", "cherry","Strawbery","Kiwi"])

#-----------------------------------------------------------------------------
#positional only-arguments= ,/ after argument

def my_function(x, /):
  print(x)

my_function(3)

#keyword argument only= * before arguments
def my_function(*,x):
  print(x)

my_function(x = 3)      # this is keyword argument


## focus on only
# positional arguments only - tuples argument only
def add(x,/):  # for single value ,/ use after argument
    sqr = x+x
    return sqr

print(add(3))

def add(x,y,z): # for multiple assignment muliple parameter used
    add = x+y+z
    return add

print(add(5,6,7))


#keyword argument only - dict values taken
def multiply(*,x,y,z):
    sqr = x*y*z
    return sqr

print(multiply(x = 3,y =2,z=1))

#-------------------------------------------------

# arg =>   *arg -- it takes only tuple as argument and parameter is only one variable
# kwarg =>  **kwarg -- it takes only dictionary as argument and parameter is only one varible
#
# ,/ => positional arguments only -- tupple-- seperate parameter have seperate argument
# *  => keyward arguments only -- dict -- seperate keyvalue pair have seperate argument


# combining the both
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)


#difference between parameter and arguments
def add(n1,n2):  # n1 and n2 are parameters
    addition = n1+n2
    print(addition)

add(10,20) # here 10 and 20 are arguments while function call


# Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
result = factorial(5)
print(result)  # Output: 120

# Lambda

var = lambda a : a + 10
print(var(100))

add = lambda w,x,y,z : w+x+y+z
print(add(10,20,30,40))

def add(w,x,y,z):
    addition = (w+x+y+z)
    print(addition)
add(10,20,30,40)


#use of lamda in function
def add(n):
    return lambda a : a + n

variable = add(100)
print(variable(500))


#-------------------------MAP-----------------------------------
lst = [10,20,30,40,50]
square = map(lambda x : x **2 ,lst )
print(tuple(square))

# map in the function
def square(x):
    squared = x **2
    print(squared)
lst = [10,20,30,40,50]
result  = map(square,lst)  # result is in object
print(list(result)

def addition(n):
    return n + n

numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))  # Output: [2, 4, 6, 8]


tuple = 10,20,30,40,50
square1 =map(lambda x : x**2,tuple)
print(list(square1))

lst1 = [10,20,50,60,90,850]
var = map(lambda a : a + 10,lst1)
print(tuple(var))

#-------------------------Filter------------------------
# Using filter() with lambda to filter even numbers
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]


def is_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels
print(is_vowel("a"))

sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
vow = filter(is_vowel,sequence )
print(tuple(vow))

#-----------------------------------------------------------------
def greater(number):
    # if number > 50:
    #     print(f"{number} is greater than 50")
    return number >50

lst = [10,20,30,40,50,60,40,1000,120,505]
result = filter(greater,lst)  # filter use to filter values based on condition
print(list(result))

lst = [10,20,30,40,50,60,40,1000,120,505]
result = map(greater,lst) # map will check function for all the element
print(list(result))

#------------------------------------------------------------------------
#given is list if numbers is even double it if odd remains same

def make_double(x):
    for i in str(x):
        if int(i) %2 ==0:
            print(int(i)*2)
        else:
            print(int(i))

lst = [2, 3, 4, 6, 7, 8, 9]
result = map(make_double,lst)
print(list(result))

#same example by using lambda
lst = [2, 3, 4, 6, 7, 8, 9]
make_double = lambda x: [int(i) * 2 if int(i) % 2 == 0 else int(i) for i in str(x)]
result = map(make_double,lst)
print(list(result))
#---------------------------------------------------------------------------
