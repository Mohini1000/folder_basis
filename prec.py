# def isprime(n):
#     for x in range(2,n):
#         if n%x==0:
#             print("not prime number")
#             break
#     else:
#         print("prime number")
# num=int(input("enter the number"))
# isprime(num)
from collections import Counter
lst = [1, 1, 2, 2, 2, 2, 3, 4, 4, 5, 6]
cnt=Counter(lst)
print(cnt)

for key, value in cnt.items():
    print(f"{key} occur {value} times")


# Output: Counter({2: 3, 1: 2, 4: 2, 3: 1, 5: 1})


# count = 0
# lst = [1, 1, 2, 2, 2, 2, 3, 4, 4, 5, 6]
#
# for i in range(len(lst) - 1):  # Avoid last index to prevent IndexError
#     if lst[i] == lst[i + 1]:
#         count += 1
#
# print("Count of adjacent duplicates:",count)
