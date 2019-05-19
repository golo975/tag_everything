#
# 读取人物名称

f = open('../name.txt')
data = f.read()
print(data.split('|'))

# 读取兵器名称
f2 = open('../weapon.txt')
i = 1
for line in f2.readlines():
    if i % 2 == 1:
        print(line.strip('\n'))
    i += 1

# f3 = open('../sanguo.txt')
f3 = open('../sanguo.txt', encoding='GB18030')
# f3 = open('../sanguo_utf8.txt')
# print(f3.read(1000))
# print(f3.read())
print(f3.read().replace('\n', ''))


def func(filename):
    f = open(filename)
    print(f.read())
    print('test func')
    f.close()


func('../name.txt')
