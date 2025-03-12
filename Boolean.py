#Booleans represent one of two values: True or False.
print(10 > 9)
print(10 == 9)
print(100 < 9)

a = 200
b = 500
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


print(bool("Hell o"))#true
print(bool(15))#true
print(bool())  # empty string is false
print(bool(0)) # 0 value also false
print(bool(1))
print(bool(-1))
print(bool(["apple", "cherry", "banana"]))



# use of bool inside the function
def myFunction() :
  return True

print(myFunction())


def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")

print(myFunction())

# isinstance function used to check the datatype stored inside a variable
x = 200
print(isinstance(x, str))


