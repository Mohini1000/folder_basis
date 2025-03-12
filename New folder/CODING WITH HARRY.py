#1) ADD TWO NUMBERS
a=int(input("enter first number"))
b=int(input("enter second number"))
sum=a+b
print(f"addition of {a} and {b}= {sum}")

#1) ADDITION OF NUMBER IN LIST
list=[370,200,10,400]
total=0
for i in range(len(list)):
    total=total+list[i]
print(total)
#--------or---------
a=[20,400,70,100]
b=sum(a)
print(b)

#2) check maximum number
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if a>b and a>c:
    print(f"{a} is maximum number")
elif b>c and b>a:
    print(f"{b} is maximum number")
else:
    print(f"{c} is maximum number")

#---------or---------
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
max= a if a>b and a>c else b if b>c and b>a else c
print(f"maximum number between {a},{b},{c} is = {max}")

#3)wap to read employee data from the keyword and the print the data
name=input("enter employee name=")
print("employee name=" ,name)
age=int(input("enter employee age="))
print("employee age=",age)
salary=float(input("enter employee salary="))
print("employee salary=",salary)
address=input("enter employee address=")
print("employee address=",address)
married=eval(input("enter marrital status-[True/False]="))
print("marrital status=",married)
#if we use bool it is not giving output for false so we use eval)
#----------------------------------------------------------
#4)multiplication of 2 no by ternary way
a,b=[int(x)for x in input("enter two numbers=").split(',')]
print("multiplication of",a,"and",b,"is=",a*b)
#------------------------------------------------------------------------

#4)to get table of 1-10 using for loop
for i in range (1,11):
    for j in range (1,11):
        print(f"table of {i}*{j}= {i*j}")
    print("-----------------------------")

# using while loop using input from customer
a=int(input("enter the number from 1 to 10 to get table"))
i=1
while i<10:
    i=i+1
    print(f"multiplication of{a}*{i}={i*a}")

#without input-direct table from 1-10

c=1
while c<=10:
    for x in range(1,11):
        print(f"table of {c}*{x}={c*x}")
    print("-----------------------")
    c=c+1

#----------------------------------------------------------------
#5)wap to read 3 float nos with - seperator and print their sum
a,b,c=[float(x) for x in input("enter three numbers").split('-')]
print("addition of",a,b,c,"is =",a+b+c)

#6)eval function
a=eval(input("enter expression"))
b=eval(input("enter expression"))
print(a)#a+b
print(b)#a*b

#7)`python program to get reminder
a=30
b=10
print("reminder when a is divide by b is=",a%b)

#8) python program to find avg of two number
a=int(input("enter first number="))
b=int(input("enter second number="))
avg= (a+b)/2
print("average of a and b is =",avg)

#9)find out square of give no by user
a=int(input("enter number="))
square=a*a
print("square of give number =",square)

#10)
name=input("enter your name \n")
print("good morning,",name)

#11)escape character
s="dear harry,this python course is nice, Thanks!"
escape_s=("dear harry,\n\t this python course is nice.\n\t thanks! ")
print(escape_s)

#12) create a list of 7 fruits by taking input from user
f1=input("enter fruit name 1:")
f2=input("enter fruit name 2:")
f3=input("enter fruit name 3:")
f4=input("enter fruit name 4:")
f5=input("enter fruit name 5:")
f6=input("enter fruit name 6:")
f7=input("enter fruit name 7:")
myfruitlist=[f1,f2,f3,f4,f5,f6,f7]
print(myfruitlist)

#13) enter mark by 6 student and display in sorted manner
m1=int(input("enter marks for student by roll no-1"))
m2=int(input("enter marks for student by roll no-2"))
m3=int(input("enter marks for student by roll no-3"))
m4=int(input("enter marks for student by roll no-4"))
m5=int(input("enter marks for student by roll no-5"))
m6=int(input("enter marks for student by roll no-6"))
student_mark=[m1,m2,m3,m4,m5,m6]
student_mark.sort()
print (student_mark)

#14)add element of list
l1=[10,40,50,70]
sum=l1[0]+l1[1]+l1[2]+l1[3]
print(sum)
#15)count of 0 in given tuple
a=[7,0,8,0,0,9]
b=a.count(0)
print(b)
#16)create dictionary of hindi word with value as english translation and provide user input to look into it
dict={"pankha":"fan","dabba":"box","vastu":"item","darwaja":"door"}
print("option for hindi word is=",dict.keys())
a=input("enter the hindi words=")
print("meaning of your word is=",dict[a]) #user input stored in variable a, so access value coorespond to a

#instead of dict[a] we prefer dict.get(a) function bcz if value is not avilable dict[a] gives error,but
#dict.get[a] gives none
print("meaning of your word is=",dict.get(a))

#17) prgm to enter eight number from user and display unique value
num1=input("enter number 1")
num2=input("enter number 2")
num3=input("enter number 3")
num4=input("enter number 4")
num5=input("enter number 5")
num6=input("enter number 6")
num7=input("enter number 7")
num8=input("enter number 8")
num9=input("enter number 9")
b={num1,num2,num3,num4,num5,num6,num7,num8,num9}# we want unique value not duplicate so we use set
print(b)

#18) can we have 18 int and "18" str in set
s={18,"18"}
print(s)
# yes we have both value bcz one is int and one is string

#19)what is length of following
s=set()
s.add(20)
s.add(20.0)# 20 and 20.0 have same value so it conside it as only one
s.add("20")
print(s)
print(len(s))#lenghth=2

#20)create an empty dictionary allow 4 friend to enter their fav lang as value and use name as key
favlang={}
a=input("enter your favourite language shubham")
b=input("enter your favourite language rutu")
c=input("enter your favourite language vishaka")
d=input("enter your favourite language durva")
favlang['shubham']=a # this is dictionary so using this we are setting value for key
favlang['rutu']=b
favlang['vishaka']=c
favlang['durva']=d
print(favlang)

#21)for above example what happen if  two friend name are same
# then it will replace previous key to latest key
#22)for above example what happen if  two friend language are same
#then it will print, bcz value can be same no issue.

#23)can you chnage value inside list which is stored in set
set={8,7,12,"harry",[1,2]}
#this set is not correct bcz we can not store list in set bcz it is chnageble, we can store tuple
# but we cant change value bcz indexing is not allowed in set and set is unorderd

#24)input age by user if age>17
a=int(input("enter your age"))
if a>18:
    print("yes")
else:
    print("no")
#25) use of is and in
a=None
if a is None:
    print("yes")
else:
    print("no")
#26)write a pgrm to find greater number entered by user for 3 number
a= input("enter first number" )
b= input("enter second number")
c= input("enter third number" )
if a>b:
    print("a is greater")
elif a>c:
    print("a is greater")
elif b>c:
    print("b is greater")
else:
    print("c is greater")

#27)write a pgrm to find greater number entered by user for 4 number
num1= int(input("enter first number" ))
num2= int(input("enter second number"))
num3= int(input("enter third number" ))
num4= int(input("enter fourth number"))
if num1>num4:
    f1=num1
else:
    f1=num4
if num2>num3:
    f2=num2
else:
    f2=num3
if f1>f2:
    print("greater number is",f1)
else:
    print("greater number is",f2)
#28) write prgm to find out student is pass or fail, if it require total 40% and at least 33%
# in each subj to pass,assume 3 subject and take input from user

sub1=int(input("enter mark of subject 1"))
sub2=int(input("enter mark of subject 2"))
sub3=int(input("enter mark of subject 3"))
if (sub1<33 or sub2<33 or sub3<33):
    print("you are failed, bcz mark is less than 33")
elif (sub1+sub2+sub3)/3<40:
    print("you are fail")
else:
    print("you are pass")

#29)spam text detector program
txt=input("enter the text")
if ("make a lot of money" in txt):
    spam=True
elif("buy now" in txt):
    spam=True
elif("click this" in txt):
    spam=True
else:
    spam=False
if (spam):
    print("this text is spam")
else:
    print("this is not spam")
#30)write prgm to find out wheteher given username contain less than 10 character or not
name=input("enter any name")
if len(name)<10:
    print("name having character less than 10")
else:
    print("name having character greater than 10")
#31) write prgm to check wheather give prgm is in list or not
list=["harry","mohini","chopra",99,"coder","nice"]
a=input("enter the string")
if a in list:
    print("yes, it is present")
else:
    print("it is not present")

#32)write prgm to calculate grade of sudent from his mark
 #80-90=A,70-80=B,60-70=C,50-60=D,<40=E
marks=int(input("enter your mark"))
if marks>90:
    grade="A"
elif marks>80:
    grade="B"
elif marks>70:
    grade="C"
elif marks>60:
    grade="D"
elif marks>50:
    grade="E"
else:
    grade="fail"
print("your grade is",grade)

#33)write pgm to find out wheather given post is talking about harry or not
post='''hi team, harry is good coder
      providing free python cource
      with notes to all people'''
if "harry" or "HARRY" in post:
    print("yes harry is present")
else:
    print("it is not present")
#34)write prgm to print no 1 to 50 using while loop
i=0
while i<50:
    print(i)
    i=i+1
#35)print "mohini" 5 times using while loop
i=0
while i<5:
    print("mohini")
    i=i+1
#36)print element in list using while loop
fruits=["apple","banana","cherry","mango"]
i=0
while i <(len(fruits)):
    print(fruits[i])
    i=i+1
#37) write program to print multiplication of given table using for loop
a=int(input("enter any digit"))
for i in range(1,11):
    print(f"{a}*{i} ={a*i}")

#38)write prgm to get all person started with s which stored in list
list=["harry","soham","sachin","rahul"]
for x in list:
    if x.startswith("s"):
        print("hello"+ x)
#39) write program to print multiplication of given table using while loop
a=int(input("enter any digit"))
i=1
while i<11:
    print(f"multiplication of {a}*{i}={a*i}")
    i=i+1

#40) write prgm to find number is prime or not
a=int(input("enter the number"))# (not understand)
prime=True
for i in range(0,a):
    if (a/i==0):
        prime=False
        break
if prime:
    print("number is prime")
else:
    print("number is not prime")

#41)write prm to find sum of first n natural no using while loop

#42) write prgm to calculate factorial of given input no using for loop

#43)print star pattern
for i in range(4):
    print("*" * (i+1))
# here we take (i+1) instead of i to print 4 times *, if we take i it gives range 0 to 3

#44)write program to print multiplication of given table in reverse order
a=int(input("enter the number"))
for i in range(0,a,-1):
    print(f"mulipication is{a}"{i})={}a*i


#**********************prgm using function************************************

#1)write prm using function to find greatest of three number
def maximum(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num3 and num2>num1:
        return num2
    else:
        return num3
max=maximum(12,22,10)
print("maximum no is",max)

#-----------------------------------------------------------------------------

#2)write python prm using function to convert celsius to fahrenheit
# formula= F = ((9/5)*C)+32

def farhen(cel):
    return((9/5)*cel+32)   #this is the formula
d=farhen(21)              #here we can give temp to which we want to convert
print("fahrenheit temperature is",d)

#---------------------------------------------------------------
#3)python prgm to prevent python print function to add new line at end

print("hii",end=' ')
print("hello",end=' ')
print("how are you",end=' ')

#--------------------------------------------------------------------
#4)prgm to convert inches to cm
#1 inch= 2.54cm

def inch_to_cm(inch):
    return(2.54*inch)       #here we can written formula

convert=inch_to_cm(4)
print("converted cm is",convert)

#---------------------------------------------------------
#6)python prgm to remove given world from string and strip it at same time

def remove_and_strip(string,word):
    newstr=string1.replace("good",'')  #using replace we replace good with space
    return(newstr.strip())

string1="  harry is a good coder  "  #strip is used to remove space at start and end
b=remove_and_strip(string1,"good")
print(b)

#---------------------------------------------------
#7)python function to print multiplication table of given number

def multiply(num):
    for i in range(1,11):
        print(f"{num}*{i}={num*i}")

multiply(5)          #this is used to call function

#---------------------------------------------------
#8)python function to print square of given number

def square(num):
    return num*num
n=int(input("enter the number"))
s=square(n)
print(s)

#9)write a function to accept 2 nos as input and return sum
def addition(a,b):
    return a+b
c=addition(4,5)
print(c)

#10)write a function to check wheather the given no is odd or even
def odd_even(a):
    if a%2==0:
        print(f"{a} is even")
    else:
        print(f"{a} is odd")

odd_even(7)

#11)write a single function which can add two numbers and also the
# same function should be able to subtracct,multiply and divide:

def number(a,b):
    addition=a+b
    print("addition=",addition)
    substraction=a-b
    print("substraction=",substraction)
    multiplication=a*b
    print("multiplication=",multiplication)
    division=a/b
    print("division=",division)
number(14,5)
