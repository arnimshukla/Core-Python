import datetime
today=datetime.date.today()
future =today+datetime.timedelta(days=10)
prev =today-datetime.timedelta(days=10)
print("after 10 days",future)
print("after 10 days",prev)