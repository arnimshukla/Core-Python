from unittest import expectedFailure

print('before')
try:
    a = 10
    b = 0
    print('mid')

    c = a / b

    print('division', c)
except ZeroDivisionError as e:

    print('after',e)
