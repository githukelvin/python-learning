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
    if (y == 3 or y == 6):
        continue
    print(y)
