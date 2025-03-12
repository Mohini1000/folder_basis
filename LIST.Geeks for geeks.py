#1) find largest element in list

arr=[10,40,80,75,92,48,1]
arr.sort()
print(arr)
print(arr[-1])

#using for loop
arr=[10,40,80,75,92,48,1]
max=arr[0]
for x in range(len(arr)):
    if arr[x] >max:
    max=arr[x]
print(max)

#---------------------------------------------------------------
#2)Check if element exists in list in Python

list=[2,8,22,11,35,6]
i=11
if i in list:
    print("yes")
else:
    print("no")

#---------------------------------------------------------------
#3)Python program to swap two elements in a list
#1st element with 2nd last element

list=[2,8,22,11,35,6]
temp=list[0]
list[0]=list[-2]
list[-2]=temp
print(list)

#--------------------------------------------------------------------------
#4)Different ways to clear a list in Python
list=[2,8,22,11,35,6]

#1)pop          pop method removed using index
list.pop(1)
print(list)

#2)remove       remove method remove specified element
list.remove(22)
print(list)

#3)del       del remove using index, no dot after del and index should be in []
del list[2]
print (list)
del list       #del also delete list completely

#4)clear   it clear list completely this remains []
list.clear()
print(list)

#-----------------------------------------------------------------------------------------

# 5)Python | Reversing a List
list=[10,"mohini",45,"priti","false",True]
print(list[::-1])

#using reverse
list.reverse()
print(list)

#for loop
for x in range(len(list)-1,-1,-1):
    print(list)

#--------------------------------------------------------------
#6)Python program to find sum of elements in list
list=[2,8,22,11,35,6]

#using function
from functools import reduce
result=reduce(lambda x,y:x+y,list)
print(result)

#using for loop
sum=0
for x in range(len(list)):
    sum=sum+list[x]
print(sum)


#above prgm we can write like below also

list=[2,8,22,11,35,6]
sum=0
for x in list:
    sum=sum+x
print(sum)

#----------------------------------------------------------

#7) Python | Multiply all numbers in the list
list=[2,8,22,11,35,6]
from functools import reduce
result=reduce(lambda x,y:x*y,list)
print(result)


#for loop
multiply=1
for x in list:
    multiply=multiply*x
print(multiply)

#--------------------------------------------------------------

#8)Python program to find smallest number in a list
list=[12,8,22,11,35,6]
list.sort()
print(list[0])

min=list[0]
for x in range(len(list)):
    if min<list[x]:
        min=list[x]
print(min)

#--------------------------------------------------------------------------

#9)Python program to find largest number in a list
list=[12,8,22,11,35,6]
list.sort()
print(list[-1])

#-----------------------------------------------------------------

#10)Python program to find second largest number in a list
list=[12,8,22,11,35,6]
list.sort()
print(list[-2])

#-------------------------------------------------------------

#11)Python program to find N largest elements from a list

list=[10,12,34,67,89,88,64,21,34]
max=list[0]
for x in range(len(list)):
    if max<list[x]:
        max=list[x]
print(max)


#-------------------------------------------------------
#12)Python program to print even numbers in a list
list=[12,8,22,11,35,6]
list1=[]
for x in list:
    if x%2==0:
        list1.append(x)
print(list1)

#--------------------------------------------------------
#13)Python program to print odd numbers in a List
list=[12,8,22,11,35,6]
list1=[]
for x in list:
    if x%2!=0:
        list1.append(x)
print(list1)

#---------------------------------------------------------------
#14)Python program to print all even numbers in a range

list=[]
for x in range(1,21):
    if x%2==0:
        list.append(x)
print(list)


#15)Python program to print all odd numbers in a range
#same like above

#---------------------------------------------------------------------
#16)Python program to print positive numbers in a list

lst=[10,-2,12,0,-22,13,8]
for x in lst:
    if x>=0:
        print(x,end=',')

#17)Python program to print negative numbers in a list

#---------------------------------------------------------------------
#18)Python program to print all positive numbers in a range
#19)Python program to print all negative numbers in a range

for x in range(-20,-1):
    print(x,end=',')

#-----------------------------------------------------------------------

#20)Remove multiple elements from a list in Python
#using slicing

list=[10,"aditya",True,29,"pratu",9]
del list[1:4]
print(list)


#21)for loop
list=[10,12,34,67,89,88,64,21,34]
for x in list:
    if x%2==0:
        list.remove(x)
print(list)

#--------------------------------------------------------------------

#22)Python – Remove empty List from List

list=[10,"mahesh",[],35,"prit",[],29]
for x in list:
    if x==[]:
        list.remove(x)
print(list)


#23)using list comprensation
list=[10,"mahesh",[],35,"prit",[],29]
newlist=[x for x in list if x!=[]]
print(newlist)

#-------------------------------------------------------------------------------
#23)Python | Cloning or Copying a list
#following way we can copy list from one to another

lst=[10,"mahesh",True,35,"prit",[],29]
copy_lst=list(lst)
print(copy_lst)


#using slicing
new_lst=lst[::]
print(new_lst)

#extend method
newlst=[]
newlst.extend(lst)
print(newlst)

#using inbuild copy
new_lst=lst.copy()
print(new_lst)

#---------------------------------------------------------------

#24)Python | Count occurrences of an element in a list



#--------------------------------------------------------
#25)Python | Remove empty tuples from a list
list=[10,20,"mohini",(),39,"poo",()]
list.remove(())      #it remove only 1st tuple
print(list)


newlst=[]
for x in list:
    if x!=(()):    #it removes both tuple
        newlst.append(x)
print(newlst)

#---------------------------------------------------------------------
#26)Python | Program to print duplicates from a list of integers

list=[10,100,35,89,100,100,100,100,23,35,78,89,23]
single_lst=[]
duplic_lst=[]

for x in list:
    if x not in single_lst:  # check for all element one by one
        single_lst.append(x)  #here if or elif single time only one loop give o/p
    elif x not in duplic_lst: #if elelm not in single list it append to single, if ele present in single
        duplic_lst.append(x)  #then go for duplic_lst and append it
print(single_lst)    #it give unique element
print(duplic_lst)     #it gives duplicate ellemnt

#if duplicate elemt 3, 4 times it only give single elelmt in duplic list
#If x is not already in single_lst, it means it’s a unique element. You append it to single_lst.
#Otherwise (if x is already in single_lst), you check if it’s not yet in duplic_lst.
# If so, you append it to duplic_lst.


#----------------------------------------------------------------
#Python program to find Cumulative sum of a list
lst=[10,20,30,40,50,60,70]    #cumulative means addition one after another
newlst=[]      #here we take addition of element means 1st elem add to 2nd then 2nd to 3rd likwise
sum=0
for x in lst:
    sum=sum+x
    newlst.append(sum)
print(newlst)


#--------------------------------------------------------
#Python | Sum of number digits in List

list=[10,100,35,89,23,35,78,]
from functools import reduce
new=reduce(lambda x,y:x+y,list)
print(new)

#using for loop
sum=0
for x in range(len(list)):
    sum=sum+list[x]
print(sum)

#----------------------------------------------------------
#Break a list into chunks of size N in Python
my_list = [1, 2, 3, 4,
           5, 6, 7, 8, 9]

for i in range(0, len(my_list), 3):
    print(my_list[i:i+3])


#------------------------------------------------------------
#Python | Sort the values of first list using second list
