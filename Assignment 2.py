#
# 1.Write a Python program to count the number of vowels in a string.

s = input("enter the string:") # india
v = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
d = {}
for char in s:  # i
    if char in v:
        d[char] = d.get(char, 0) + 1
        print(d)
for k, v in sorted(d.items()):
    print(k,v)


    print('{} occurs {} times'.format(k, v))


from functools import reduce
lst=[2,3,4,5,6,7,8,9]

result=map(lambda x:x*2,lst)
print(list(result))

result1=filter(lambda x:x%2==0,result)
print(list(result1))

result2=reduce(lambda x,y:x+y,result1)
print(result2)









# 2.Write a Python program to find the sum of all even numbers from 1 to N.

num = int(input("Enter the number upto which you want even number"))
sum =0
for i in range(1,num+1):
  if i % 2 == 0:
    sum = sum + i
print(sum)







# 3.Write a Python program to count the occurrences of a specific character in a string.
string = input("enter the string")
''' india==  i comes 2 times
n comes 1 time'''

dictionary = {}
for element in string:
  element = element.lower()
  dictionary[element]= dictionary.get(element,0)+1
print(dictionary)
for keys ,values in dictionary.items():
  print(f"{keys} occurs {values} times")


# 4.Write a Python program to find the second largest element in a list.
list = [10,20,30,40]
new_list = sorted(list,reverse=True)
print(new_list[1])


# 5.Write a Python program to check if two strings are anagrams of each other.
'''eg. abcd = cbda'''

str1 = input("enter str1: ")
str2 = input("enter str2: ")

if len(str1) == len(str2):
  sorted_str1 = sorted(str1)
  sorted_str2 = sorted(str2)
  if sorted_str1 == sorted_str2:
    print(f"{str1} and {str2} are anagrams")
  else:
    print(f"{str1} and {str2} are not anagrams")
else:
    print(f"{str1} and {str2} are not anagrams")



# 6.Write a Python program to convert Celsius to Fahrenheit.
# Lambda function to convert Celsius to Fahrenheit
convert_to_fahrenheit = lambda celsius: (celsius * 9/5) + 32

# Example usage:
celsius_temperature = 25
fahrenheit_temperature = convert_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature}°C is approximately {fahrenheit_temperature}°F")



# 7.Write a Python program to check if a year is a leap year.
year = int(input("enter the year: "))

if year % 4 ==0 or year %100 == 0 :
  print(f"The {year} is leap year")
else:
  print(f"The {year} is not leap year")


# 8.Write a Python program to generate Fibonacci series up to N.
num1 = int(input("enter the first number: "))
num2 = int(input("enter the first number: "))
num3 = int(input("enter the first number: "))

maximum = ((num1 if num1>num2 else num2) if num1 > num3 else num3)
print(f"The maximun number is {maximum}")



# 9.Write a Python program to find the GCD (Greatest Common Divisor) of two numbers.
num1 = int(input("Enter the number1"))
num2 = int(input("Enter the number2"))

lst1=[]
lst2=[]

for i in range(2, num1):
  if num1 % i == 0:
    lst1.append(i)

for j in range(2, num2):
  if num2 % j == 0:
    lst2.append(j)




# 10.Write a Python program to find the LCM (Least Common Multiple) of two numbers.
# 11.Write a Python program to find the area of a triangle given its base and height.
# 12.Write a Python program to find the factors of a number.
# 13.Write a Python program to check if a number is an Armstrong number.
# 14.Write a Python program to find the sum of digits of a number.
# 15.Write a Python program to check if a number is a perfect number.
# 16.Write a Python program to find the ASCII value of a character.
# 17.Write a Python program to check if a string contains only digits.
# 18.Write a Python program to remove duplicates from a list.
# 19.Write a Python program to find the intersection of two lists.
# 20.Write a Python program to find the union of two lists.
# 21.Write a Python program to find the difference between two lists.
# 22.Write a Python program to find the median of a list of numbers.
# 23.Write a Python program to find the mode of a list of numbers.
# 24.Write a Python program to sort a list of numbers.
# 25.Write a Python program to swap two variables.
# 26.Write a Python program to check if a number is prime.
# 27.Write a Python program to find the factorial of a number.
# 28.Write a Python program to reverse a string.
# 29.Write a Python program to check if a string is a palindrome.
# 30.Write a Python program to find the largest element in a list.
# 31.Write a Python program to find the sum of elements in a list.
# 32.Write a Python program to find the length of a string.
# 33.Write a Python program to find the maximum of three numbers.
