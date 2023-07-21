stdHeights = input("input a list of student heights ").split(",")
sum = 0
avg= 0
for n in range(0, len(stdHeights)):
    stdHeights[n]=int(stdHeights[n])
    sum +=stdHeights[n]
    avg = round(sum/len(stdHeights))
print(avg)