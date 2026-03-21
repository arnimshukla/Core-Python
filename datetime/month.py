import datetime
for i in range(1,13):
    month=datetime.date(2020,i,1).strftime('%B')
    print(f' {i}:{month}')
