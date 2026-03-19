list=[100,22,9,21,2,23,4]
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i] > list[j]:
            t=list[i]
            list[i]=list[j]
            list[j]=t
    print(list[i])

