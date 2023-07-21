row1 = ['☮', '☮', '☮']
row2 = ['☮', '☮', '☮']
row3 = ['☮', '☮', '☮']
print(f"   1     2    3")
print(f"1{row1}\n2{row2}\n3{row3}")
mapped = [row1, row2, row3]

position = input("where do you want to put the treasure ?")
print(position[0])

mapped[int(position[1])-1][int(position[0])-1] = '💢'

print(mapped)
print(f"   1     2    3")
print(f"1{row1}\n2{row2}\n3{row3}")
