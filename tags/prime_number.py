"""100以内的所有质数"""

for i in range(2, 101):
    for j in range(2, i + 1):
        if i != 2 and i % j == 0:
            # print(str(i) + '可以被' + str(j) + '整除，所以 ' + str(i) + '不是质数')
            break
        if j > i // 2:
            print(str(i) + ' 是质数')
            break

dict0 = {'name': 'Tom', 'age': 11}
print(dict0)

dict1 = dict(name='Tom', age=11)
print(dict1)

dict2 = dict(zip(['name', 'age'], ['Tom', 11]))
print(dict2)
