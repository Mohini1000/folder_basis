#2) assume input string contain alphabet and digits
# wap to sort character of string ,first alphabet by digits
# Output:
# ABCZ12348

input="A3C1B2Z84"
letter=""
number=""
for x in input:
    if x.isalpha()==True:
        letter=letter+x
    if x.isdigit()==True:
        number=number+str(x)   #if we give number+x it give addition of no so we convert x into string
print(letter)
print(number)

sort_letter=sorted(letter)
sort_number=sorted(number)
print(sort_letter)  #output=['A', 'B', 'C', 'Z']
print(sort_number)  #output=['1', '2', '3', '4', '8']
                    #it gives output like list, so we have to join both string

join_letter="".join(sort_letter)
join_number="".join(sort_number)
print(join_letter)
print(join_number)

output=join_letter + join_number
print("output=",output)

#sorted(list) it return new copy of list without changing original list
#sorted() used for sorting list ,dictionary,string,tuple
#list.sort() sort the original list and replace it

#for reverse
# mylist = reversed(sorted(mylist))
# or
# mylist = sorted(mylist, reverse=True)

#----------------------------------------------------------------------


#3)input=a4b3c2
#  output=aaaabbbcc


input="a4b3c2"
output=''
for x in input:
    if x.isalpha()==True:
        alph=x               #if x is alphabet it stored in alph
    if x.isdigit()==True:
        digi=int(x)          # if x in digit it stored in digi, we convert string x into integer x
        output=output+alph*digi      #multiplication(a*4)=aaaa+b*3+c*2
print(output)

#In Python, you can use multiple if statements without an else part

#------------------------------------------------------------------

#4)input= 'a4k3b2'
#output="aeknbd"

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

#print(ord(char))  # ord gives us unicode of this number
#newchar = chr(100)  # chr gives unicode to letter


#5)remove duplicate charcter's from the given string:
#output="AZCFGH"

s='AAAAAAAAAAAAAZZZZZZZZZCCCCCCCCFFFFFFFFFGGGGHHH'
s1=set(s)
for x in s1:
    print(x,end=',')             #set does not allow duplicate value,so we convert it into set


#----------------------------

s='AAAAAAAAAAAAAZZZZZZZZZCCCCCCCCFFFFFFFFFGGGGHHH'
output=''
for x in s:
    if x not in output:
        output=output+x
print(output)

#--------------------------

s='AAAAAAAAAAAAAZZZZZZZZZCCCCCCCCFFFFFFFFFGGGGHHH'
output=''
for x in range(0,len(s)):
    if s[x] not in output:
        output=output+s[x]
    else:
        continue
print(output)


#--------------------------------------------
# ord is used to get ascii value of character
#chr used to give character of ascii value

print(ord("a"))
print(chr(100))

#6)given string ,get ascii value for all

a="hello world"
list=[]
for x in a:
    y=ord(x)          #to get ascii value of all letter in a
    list.append(y)
print(list)

for element in list:
    z=chr(element)   #to get character of no in list
    print(z,end=',')

#-----------------------------------------------------------
