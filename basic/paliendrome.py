number =  123
r = 0
rev = 0
n = number # n = 153

while n > 0: # n = 153, n = 15, , n = 1
    r = n % 10 # r = 153 % 10 = 3, r = 15 % 10 = 5, r = 1 % 10 = 1
    rev = (rev * 10) + r  # rev = (0 * 10) + 3 = 3, rev = (3 * 10) + 5 = 35, rev = (35 * 10) + 1 = 351
    n = n // 10 # n = 153 // 10 = 15, n = 15 // 10 = 1, n = 15 // 10 = 0

if number == rev:
    print('palindrome number',rev)
else:
    print('not palindrome number',rev)