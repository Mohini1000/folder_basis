# 1) Python program to check if a string is palindrome or not
str=input("enter the string")
new_str=""
for x in str:
    new_str=x+new_str
if new_str==str:
    print("string is palindrome")
else:
    print("string is not palindrome")

#using slicing

str=input("enter the string")
new=str[::-1]
if str==new:
    print("string is palindrome")
else:
    print("string is not palindrome")



#-----------------------------------------------------------------

#2) Python program to check whether the string is Symmetrical or Palindrome

#  A string is said to be symmetrical if both the halves of the string are the same
# and a string is said to be a palindrome string if one half of the string is the reverse of
# the other half or if a string appears same when read forward or backward.

#symmetrical string and no palindrome= khokho
#symmetrical string and  palindrome= ammaamma

str=input("enter the string")
half=int(len(str)/2)     #divide string into half
first=str[:half]        #check str start with o and end point is half of string
last=str[half:]         #second part start with half and end with last
if first==last:
    print("string is symmentrical")
else:
    print("string is not symmetrical")
if first==last[::-1]:
    print("string is palindrome")
else:
    print("string is not palindrome")



#-------------------------------------------------------------

# 3)Reverse words in a given String in Python
str="learning python is very easy"
b=str[::-1]
print(b)


str="learning python is very easy"
rev_str=''
for x in str:
    rev_str=x+rev_str
print(rev_str)


#-------------------------------------------------------------------------
#4) Ways to remove i’th character from string in Python
str="learning python is very easy"
new_str=str.replace("e","")
print("string after removing e= ",new_str)  #it remove all occurence of that letter from string


str="learning python is very easy"
new_str=str.replace("e","",1)# here 1 is for one occurence
print("string after removing e= ",new_str)  #it remove only 1st occurence of that letter from string


#--------------------------------------------------------------------------

#5) Python | Check if a Substring is Present in a Given String

str="learning python is very easy"
substr="python"
for x in str:
    if substr in str:
        print("substring is present")
    else:
        print("substring is not present")



text = "Geeks welcome to the Geek Kingdom!"
if "Geeks" in text:
    print("substring is present")
else:
    print("substring is not present")

#----------------------------------------------------------------------

#6) Python – Words Frequency in String Shorthands

#------------------------------------------------------------------------------
# 7)Python – Convert Snake case to Pascal case

# We can replace underscores with spaces, then apply title case to each word,
# and finally remove the spaces.

snake_str = 'geeks for geeks_is_best'
pascal_str=snake_str.replace("_"," ").title()
print(pascal_str)

#-------------------------------------------------------
#8) Find length of a string in python (4 ways)

text = "Geeks welcome to the Geek Kingdom!"
counter=0
for x in text:
    counter=counter+1
print(counter)

#------------------------------------------------------------------

#9) Python program to print even length words in a string
#to get output as txt having length even

text = "Geeks welcome to the Geek Kingdom!"
s=text.split(" ")
for x in s:
    if len(x)%2==0:
        print(x,end=' , ')


#using lambda

text = "Geeks welcome to the Geek Kingdom!"
s=text.split(" ")
even=filter(lambda x:(len(x)%2)==0,s)
print(list(even))

#here we can not use map bcz map give output for all element,so we use filter


#-------------------------------------------------------------------------------------
# 11) Python program to accept the strings which contains all vowels

# txt=input("enter the string")
# vowel=("a","e","i","o","u")
# for v in vowel:
#     if v in txt:
#         print("all vowel are present")
#     else:
#         print("all vowel are not present")

#------------------------------------------------------------------------------


#12) Python | Count the Number of matching characters in a pair of string

string1="hellopriya"
string2="hellogm"
lst=[]
for x in string1:
    if x in string2:
        lst.append(x)
print("no of letter which occur repeatedly=",len(lst))

#---------------------
#same question in lst
lst1=[2,4,6,8,7,9]
lst2=[1,2,3,4,5,6]
b=0
for x in lst1:
    if x in lst2:
        b=b+1
print(b)
#-----------------------

#using dictionary
str1 = "aabcddekll12@"
str2 = "bb2211@55k"
dict={}
for x in str1:
    if x in str2:
        dict[x]=dict.get(x,0)+1
for k,v in (dict.items()):
    print(f"{k} occur {v} times")

#using set method
string1="VISHAV"
string2="VANSHIKA"
b=len(set(string1).intersection(set(string2)))
print("total no of common character is=",b)


#-----------------------------------------------------------------------
# 13) Remove all duplicates from a given string in Python
string="hellopriyahellogm"
str=set(string)
print(str)


string="hellopriyahellogm"
str1=""
for x in string:
    if x not in str1:
        str1=str1+x
print(str1)

#-----------------------------------------------------------------------------------------

#14) Python – Least Frequent Character in String
#15) Python | Maximum frequency character in String

#----------------------------------------------------------------------------
#16) Python | Program to check if a string contains any special character

#here we creat set that is normal character which should be allowed in string

allowed_char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
string=input("enter the string=")
for x in string:
    if x not in allowed_char:
        print("string contain special char")
        break
else:
    print("string not contain special char")


#another mathod is instead of defining allowed char we give special character to check
def allowed_char(txt):
    special_chars = "@_!#$%^&*()<>?/|}{~:"

    for x in txt:
        if x in special_chars:
            print("special character present in string")
            return
    print("no special character in string")

usr_input=input("enter the string")
allowed_char(usr_input)

#------------
#EASIEST METHOD

string=input("enter the string=")
for x in string:
    if x.isalnum()==False:
        print("string contain special character")
        break
else:
    print("string  not contain special char")

#---------------------------------------------------------------------
#17) Generating random strings until a given string is generated

#------------------------------------------------------------------


#18) Find words which are greater than given length k
text="Geeks welcome to the Geek Kingdom!"
b=text.split(" ")
k=3
str=""
for x in b:
    if len(x)>k:
        str=str+x    #it is not giving proper output
print(str)

#so we use list comprensation
text="Geeks welcome to the Geek Kingdom!"
b=text.split(" ")
k=3
new=[x for x in b if len(x)>k]
print(new)



#----------------------------------------------------------------------

#19) Python program for removing i-th character from a string
text = "Geeks welcome to the Geek Kingdom!"
new=text.replace("e","")
print(new)


#---------------------------------------------------------------


#20) Python program to split and join a string

text = "Geeks welcome to the Geek Kingdom!"
txt=text.split(" ")
new='-'.join(txt)
print(new)


#----------------------------------------------------------------------

#21) Python | Check if a given string is binary string or not
def binary_string(text):
    user_input=input("enter the string")
    bine="01"
    for x in user_input:
        if x not in bine:
            print("string is not binary")
            break
    else:
        print("string is binary")
binary_string("user_input")



#we can do same prgm without using function also with for loop also we can use break

user_input=input("enter the string")
bine="01"
for x in user_input:
    if x not in bine:
        print("string is not binary")
        break
else:
    print("string is binary")


#--------------------------------------------------------------------------
#22) Python program to find uncommon words from two Strings

str1="apple,banana,mango"
txt1=str1.split(",")
str2="banana,fruits,mango"
txt2=str2.split(",")
list=[]
for x in txt1:
    if x not in txt2:
        list.append(x)
for x in txt2:
    if x not in txt1:
        list.append(x)
print(list)


#----------------------------------------------------------------------------------

# 23) Python – Replace duplicate Occurrence in String

# remove  and replace duplicates
replace_dict = {"Chaitanya":"He","engineer":"Analyst"}
strng ="Chaitanya is test engineer. Chaitanya is also data engineer. Chaitanya also infoscion"

def replace_duplicates(testing_string,replace_dict):
  splited_string= strng.split()  # list- []
  empty_set = set()
  for indexes, elements in enumerate(splited_string): #enumerate used to give element with index
    if elements in replace_dict:
      if elements in empty_set:
        splited_string[indexes] =replace_dict[elements]
      else:
        empty_set.add(elements)
  return " ".join(splited_string)

result = replace_duplicates(strng,replace_dict)
print(f"The string after replacing is=== {result}")

#------------------------------------------------------------------------------
#24) Python – Replace multiple words with K

string='Geeksforgeeks is best for geeks and CS'
list_word=["for","geeks","cs"]   #we have to replace this world from string
text='gfgg'                      #with this

for x in list_word:
        string=string.replace(x,text)
print("string after chnages=",string)



string="learning python is very easy but more pratice needed"
replce_world= "is", "easy", "more"
txt="hello"
print("original string is=",string)

for x in replce_world: #this is imp firstly check element in replce_world and then check element in string
    if x in string:
        string=string.replace(x,txt)
print("string after replacing= ",string)

#--------------------------------------------------------------------
#25) Python | Permutation of a given string using inbuilt function

#-------------------------------------------------------------------------

#26) Python | Check for URL in a String
#this code is used to give url if it present in the string


string='''https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles 
in the portal of https://www.geeksforgeeks.org/'''
text=string.split(" ")
list=[]
for x in text:
    if x.startswith("https://") or x.startswith("http://"):
        list.append(x)
print("url found",list)


#---------------------------------------------------------------------------
#27) Execute a String of Code in Python

#inside the string we have written code, and it will execute using eval function

code='"hello" + "world"'
b=eval(code)
print(b)


code='3+5'
b=eval(code)
print(b)

#----------------------------------------------------------------------

# 28)String slicing in Python to rotate a string
#29) String slicing in Python to check if a string can become empty by recursive deletion

#--------------------------------------------------------------------------------
#30) Python Counter| Find all duplicate characters in string

string='Geeksforgeeks is best for geeks and CS'


#----------------------------------------------------------------

#31) Python – Replace all occurrences of a substring in a string

string='Geeks for geeks is best for geeks and CS'
string.split(" ")
substring="geeks"
if substring in string:
        string=string.replace(substring,"yellow")
print(string)

#in above question we replace single word, and below we replace many words with single letter

string='Geeks for geeks is best for geeks and CS'
string.split(" ")
replace_word="geeks","best","cs"    #main difference is here, mark every word seperateily  "",""
new="beautiful"
for x in replace_word:
    if x in string:
        string=string.replace(x,new)
print(string)


