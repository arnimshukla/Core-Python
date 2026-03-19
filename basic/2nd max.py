list = [2, 11, 23, 34, 33, 4, 43]
num = 0
second=0
for i in list:
    if i > num:
        second=num
        num = i
    elif i > second  and i!=num:
        second=i

print(second)
