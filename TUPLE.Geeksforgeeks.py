
#1)Python program to Find the size of a Tuple
import sys
tup=("mahi",29,True,"shiva",33)
print("size=",sys.getsizeof(tup),"bytes") #in tuple we can not use length function,
                                          #sys.getsizeof()    used to give size in bytes


#----------------------------------------------------------------------
#2)Python – Maximum and Minimum K elements in Tuple

tup=(20,34,89,100,125,12,34,9)
min=tup[0]
max=tup[0]
for x in range(0,len(tup)):
    if min>tup[x]:            #20>12 then min=12 like this
        min=tup[x]
    elif max<tup[x]:
        max=tup[x]
print("minimum value is",min)
print("maximum value is",max)

#--------------------------------------------------------------

#3) Create a list of tuples from given list having number and its cube in each tuple

#Given a list of numbers of list, to create a list of tuples having
# first element as the number and second element as the cube of the number.

#using function
lst=[1,2,3,4,5]
result=map(lambda x:(x,x*x*x),lst)
print(list(result))


#using list compresnsation
list=[1,2,3,4,5]
y=[(x,x*x*x) for x in list]
print(y)

#--------------------------------------------------------------

#4) Python – Adding Tuple to List and vice – versa
tup=(2,4,6,8)
lst=[12,23,45,69]
result=lst+list(tup)
print(tuple(result))

#-------------------------------------------

#5) Python – Closest Pair to Kth index element in Tuple
#6)Python – Join Tuples if similar initial element
#7) Python – Extract digits from Tuple list

#---------------------------------------------------------
#8) Python – All pair combinations of 2 tuples

tup1=(4,5)
tup2=(6,7)
result=[(a,b) for a in tup1 for b in tup2]+[(a,b) for a in tup2 for b in tup1]
print("all possible combination of tup1 and tup 2",result)

#------------------------------------------------------------
# Python – Remove Tuples of Length K
#remove tuple of specific length
tup=((2,4),(3,5,6),(1,2,3),(4,5))

result=[x for x in tup if len(x)!=2]
print(tuple(result))

#----------------------------------------------------------
# Sort a list of tuples by second Item
# Python program to Order Tuples using external List
# Python – Flatten tuple of List to tuple
# Python – Convert Nested Tuple to Custom Key Dictionary
