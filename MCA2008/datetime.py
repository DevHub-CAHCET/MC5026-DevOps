import datetime
dt=datetime.datetime.today()
print('current date:{}/{}/{}'.format(dt.day,dt.month,dt.year))
print('current date:{}:{}:{}'.format(dt.hour,dt.minute,dt.second))

from datetime import *
d=date(2021,9,12)
t=time(8,44)
dt=datetime.combine(d,t)
print(dt)
