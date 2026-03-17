num = 153
r=0
sum=0
n=num
while n>0:
    r=n%10
    sum=sum+(r*r*r)
    n=n//10
if num==sum:
    print("Armstrong no")
else:
    print("not Armstrong no")
