# for loop

str = "chaitanya"
for words in str:
    print(words)

lst = [ "chaitanya",'nagare',52,100,True]
for elements in lst:
    print(elements)

tup = ( "chaitanya",'nagare',52,100,True)
for elements in tup:
    print(elements)

for numbers in range(1,1001)  :
    print(numbers)

for numbers in range(0,1001,10)  :
    print(numbers)

lst = [ "chaitanya",'nagare',52,100,True] # len(list) = 5
for elements_indexes in range( 0 , len(lst),2):
    print(lst[elements_indexes])


# while loop
a = 0    # initial condition
while a < 99 :  # if condition is true then it goes further otherwise it come out from loop
    a = a + 3
    print(a)


for numbers in range(1,11):   # 1-10
    print("---------------------------------------------------------")
    for rows in range(1,11):   # 1 -10
        print("The table of" ,numbers, "and their product is", numbers ,'*', rows,'is', numbers *rows)





