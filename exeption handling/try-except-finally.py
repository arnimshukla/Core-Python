try:
    # Code jisme error aasakta hai
    a = 10
    b = t
    c = a / b
    print('division:', c)
except ZeroDivisionError as e:
    print('exception:', e)
except ValueError:
     print("Please number hi daalna tha")
except Exception as e:
    print('exception:', e)
else:
    print('else block executed')
finally:      #always chalta he execution ko closs krne kke  liye
    print('finally block executed')