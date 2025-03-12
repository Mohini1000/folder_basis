#1)TO CHECK NUMBER IS PRIME OR NOT

#prime no= 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
'''prime no=divided by 1 and that no (itself) only    % used for reminder after division
break can be used with for loop and while loop
'''

n=int(input("enter the number= "))
if n<2:
    print(f" {n} is not prime number")  #this is for 0,1
if n>=2:                          #start with 2 and end point=num,
    for x in range(2,n):         #n we take bcz range always take upper limit-1 so it is n-1
        if n%x==0:               #if num=6 then 6 divide by 2,3,4,5, if we get reminder 0,it break the loop
            print(f" {n} is not prime no")   #so loop will not continue till end
            break                           # so we have to take else statement out of if loop, if it inside for
    else:                                  #loop, for every division it will give result like prime,not prime
        print(f" {n} is  prime number")

#-----------------------------------------------------------------------

#2)#table of 1-10 using for loop
for x in range(1,11):
    for y in range(1,11):
        print(f"multiplication of{x}*{y}={x*y}")
    print(f"------table of {x+1}-----------")


#using  input by user
n=int(input("enter the number"))
for x in range(1,11):
    print(f"multiplication of {n}*{x}= {n*x}")

#table of 1-10 using while loop

num=1
while num<=10:
    multiplier=1
    while multiplier<=10:
        print(f"multiplication of {num}*{multiplier}= {num*multiplier}")
        multiplier=multiplier+1
    print("-----------------------------")
    num=num+1

1) Input : "a,b,c are alphabets" output : ["a","b","c","are","alphabets"], [",",",",","," "]

#-----------------------------------------------------------------------

#2)program for leap year
# main point year should be divide by 4 to get leap year
#for centuary year it should be divide by 400 to get leap year
#to check it is centuary year or not  try by divide by 100

n=int(input("enter the year"))
if (n%4==0) and (n%100!=0):
    print(f"{n} is a leap year")
elif (n%100)==0 and (n%400==0):
    print(f"{n}  is leap year")
else:
    print(f"{n} is not leap year")

#--------------------------------------------------------------

#3)program to find factorial

n=int(input("enter the number= "))
if n<0:
    print(" factorial does not exist for negative number")
elif n==0:
    print("factorial of 0 = 1")
else:
    factorial=1
    for i in range(1,n+1): # we take n+1 bcz range evaluate till 1,n
        factorial=factorial*i  #initially factorial=1, then 1*i(2)=2,so factorial 2 then fact=2*i(3) is 6
    print(f"factorial of {n}= {factorial}")

#4! = 1 * 2 * 3 * 4  = 24
# Inside the loop, the variable i takes on the values from 1 to num.
# At each iteration, the value of factorial is updated by multiplying it with the current value of i.
# For example, if num is 4, the loop will multiply factorial by 1, then by 2, then by 3, and finally by 4.

#--------------------------------------------------------------------

#4)to get first letter of all element in list
words=["balaijai","Nag","venkatesh","Mahesh"]

#using list comprensation
l=[x[0] for x in words]
print(l)

#for loop
for x in words:
    print(x[0],end=' , ')

#5) to get last letter
x[-1]

#---------------------------------------------------------------
#TUPLE

t=()
print(type(t)) #empty tuple

t=(10,20)
print(type(t))

t=10,20,30,40
print(type(t))  #this is tuple

t=10,
print(type(t)) #this is tuple

t=(10,)
print(type(t))

t=(10,20,30)
print(type(t))

t=(10)
print(type(t))# this is int, all above are tuple


#********************STAR PATTERN PROGRAM******************************************


# increase=i+1
# decrease=(i,n)

#1)python prgm to print * in square format

n=5
for i in range(n):       #outer loop for rows
    for j in range(n):   #inner loop for column
        print("*",end="  ")
    print()


#2) increasing triangle pattern (j=i+1)
n=5
for i in range(n):     #outer loop for row
    for j in range(i+1): #inner loop for column
        print("*",end=' ')  #it is like 1st row, 1column, 2nd row-2column,3rd row-3 column
    print()

#3)decreasing triangle pattern (j=(i,n)

n=5
for i in range(n):  #0,1,2,3,4   #outer loop for row
    for j in range(i,n): #(0,5)then (1,5) then (2,5) #inner loop for column
        print("*",end=' ')   #so above line print * in decreasing order
    print()

#4) increasing space and decreasing star
#   *****
#   ****
#   ***
#   **
#   *
#

n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    for j in range(i+1):
        print("",end=" ")
    print()

#5)inverted triangle pattern    increasing space and decreasing star (top to low)
# ******
#  *****
#   ****
#    ***
#     **
#      *

n=5
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ') #here we need 2 space after print('  ') to get correct pattern
    for j in range(i,n):
        print('*',end=' ')
    print()

#6)hill pattern (3 triangle)

# 1)decreasing space
# 2)increasing star
# 3)increasing star

n=5
for i in range(n):
    for j in range(i,n):
        print('',end='  ') #here we give extra space after end='  ' to get correct pattern
    for j in range(i):      #to decrease 1 column of(*) we give only i instead of i+1
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()

#7)reverse hill pattern
# 1)increasing space
# 2)decreasing star
# 3)decreasing star

n=5
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ') #after print we give extra spcae print('  ') to pattern look correct
    for j in range(i,n-1): # we decrease pattern by 1
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()


#*******************************************************************************

#5)replace the multiple of three by speaking Fizz,
# the multiple of 5 by Buzz and the multiple of 3 and 5 both by calling out FizzBuzz.
# The rest of the numbers should be called as it is with no change.
#means from 1-20 no if that no dividede by 3 or 5 not particular no..check for all no

n=int(input("enter the number"))
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)

#--------------------------------------------------------------------------
#6)python prgm to swap two variable

x=int(input("enter the variable x"))
y=int(input("enter the variable y"))

temp=x
x=y
y=temp

print(f"after swapping value of x is={x}")
print(f"after swapping value of y is={y}")

#------------------------------------------------------------
#7)Simple Python program to find sum of series
# with cubes of first n natural numbers

list=[]
sum=0
for x in range(1,10):
    sum=sum+(x*x*x)
print(sum)


from functools import reduce
arr=[12,3,14,5]
result=sum(arr)
print(result)
