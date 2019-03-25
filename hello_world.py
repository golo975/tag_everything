import os

file = open('d:/glt/data.txt', 'w')

file.write('Hello file world! \n')
file.write('Bye file world. \n')
file.write('Bye file world. \n')

file.close()

file = open('d:/glt/data.txt', 'r')
lines = file.readlines()
for line in lines:
    print(line, end='')
file.close()

file = open('d:/glt/data.txt')
for line in file:
    print(line, end='')
file.close()

file = open('d:/glt/data.txt', 'w', encoding='utf-8')
for (dir, subdirs, files) in os.walk("D:\新建文件夹"):
    print('[' + dir + ']')
    file.write(dir + '\n')
    for fname in files:
        print(os.path.join(dir, fname))
        file.write(os.path.join(dir, fname) + '\n')
