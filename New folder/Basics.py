
# Chaining the relationship operator
print(10<20)
print(10<20<30)
print(10<20<30<40)
print(10<20<30<40>50)
print(10<20>30<40)

print(10==10)
print(10!=20)
print(10==True)
print(False== False)
print('Mahaesh'=='Mahesh')
print(10=="mahesh")
#-----------------------------------------

# Ternary operator
a,b =10,20
x = 30 if a<b else 40
print(x)   #if a<b then x =30 else 40

# This is general if else statement syntax
a,b =10,20
if a < b:
    print(30)
else:
    print(40)

#-------------------------------------------------------------------------------------
# Program for maximum 3 numbers by taking input from customer using ternary operators
num1 = int(input('input from customer: '))
num2 = int(input('input from customer: '))
num3 = int(input('input from customer: '))


Maximum_Number = (num1 if num1 > num2 else num2) if num1 > num3 else num3
print("Maximum number from from customer inputs is", Maximum_Number)
#------------------------------------------------------------------------------------------
#List data types:
'''if we want to represent a group a values as a single entity where insertion order is required to preserve and duplicate
are allowed then we can use lists;
1.insertion order is preserved
2.


'''

print([10,10.5,'Mahesh',True,30])

a =[10,10.5,'Mahesh',True,30]
print(a)

print(a[0])
print(a[2:])
print(a[:-1])
print(a[:])
print(a[1:4])
print(a[1:4:2])
print(a[1:4:-2])
print(a[1:4:-1])
print(a[1:45])  # we can give upper index anything i.e greater than actual index

# operators
print(5 + 4 - 7 + 3)

# 1.aritmatic operator
a = 10
b = 3

# Addition
print('Sum:', a + b)  # Output: 9

# Subtraction
print('Subtraction:', a - b)  # Output: 5

# Multiplication
print('Multiplication:', a * b)  # Output: 14

# Division
print('Division:', a / b)  # Output: 3.5

# Floor Division
print('Floor Division:', a // b)  # Output: 3

# Modulo
print('Modulo:', a % b)  # Output: 1

# Exponentiation
print('Power:', a ** b)  # Output: 49

# 2.Assignment operators
# Assign 10 to 'a'
a = 10

# Assign 5 to 'b'
b = 5

# Add 'b' to 'a' and assign the result back to 'a'
a += b
print(a)  # Output: 15

b -=a   # here assignment operaotor fails
print(b) # -10
print(a)  # 15

b -=5   # here is right solution
print(b) # -15
print(a) # 15

b*=a
print(b) #225
print(a)  #15

#3. comparison operator
a = 10
b = 3
# Equal to operator
print('a == b =', a == b)  # Output: False

# Not equal to operator
print('a != b =', a != b)  # Output: True

# Greater than operator
print('a > b =', a > b)  # Output: True

# Less than operator
print('a < b =', a < b)  # Output: False

# Greater than or equal to operator
print('a >= b =', a >= b)  # Output: True

# Less than or equal to operator
print('a <= b =', a <= b)  # Output: False

# 4. Logical Operators Example
p = True
q = False
print("AND:", p and q)      # Output: False
print("OR:", p or q)        # Output: True
print("NOT:", not p)        # Output: False

a = (10 < 5) # false
b = (10 ==10)  # true
print(a,b)  # false , true
print(a and b) # and maily focuss on false
print(a or b) # or mainly focuss on true
print(not a)

# Complex Logical Operators Example 4
a = 85
b = 90
c = 80

x = (a>b and  b>c and c<a or a>c)
#(false and true  and true) or  true
print(x)




