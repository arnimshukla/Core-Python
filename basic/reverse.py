num = 123
r=0
reversed=0
n=num
while n>0:
    r=n%10
    reversed=(reversed*10)+r
    n=n//10
    print(reversed)
