import time

print(time.time())

print('%f' % time.time())

print(time.localtime(time.time()))

print(time.asctime(time.localtime(time.time())))

print(time.strftime('%y-%m-%d', time.localtime()))
