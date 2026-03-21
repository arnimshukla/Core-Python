import datetime
dob=datetime.date(2004,3,28)
today=datetime.date.today()
age=today.year - dob.year
print(age)