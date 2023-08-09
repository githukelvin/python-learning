import sys

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # declaration tuple

num_sum = 0
count = 0

for x in numbers:
    num_sum += x
    count += 1
    if count == 5:
        break
print(f"sum of first, {count},integer is :  {num_sum}")

for y in range(7):
    if y == 3 or y == 6:
        continue
    print(y)
# !/usr/bin/python3
for letter in 'Python':
    if letter == 'h':
        pass
        print('This is pass block')
    print('Current Letter :', letter)
print("Good bye!")

num = 2
exp = 3
product = 1
for eachpass in range(exp):
    product *= num
    # print(product, end=" ")

lis = [1, 2, 3, 4]
it = iter(lis)  # this builds an iterator object
print(next(it))  # prints next available element in iterator
# Iterator object can be traversed using regular for statement
# !usr/bin/python3
# for x in it:
#     print(x, end=" ")
# or using next() function
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()  # you have to import sys module for this


def simple():
    for j in range(10):
        if (j % 2 == 0):
          yield j

# simple()
#     Successive function call using for loop
for i in simple():
    print(i)
