#
try:
    year = int(input('input year:'))
except ValueError:
    print('年份应该输入数字')
finally:
    print('无论对错，都要执行我')

try:
    print(1 / 0)
except ZeroDivisionError as e:
    print('0不能做除数 %s' % e)
