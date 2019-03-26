import os

# file = open('d:/glt/data.txt', 'w')
#
# file.write('Hello file world! \n')
# file.write('Bye file world. \n')
# file.write('Bye file world. \n')
#
# file.close()
#
# file = open('d:/glt/data.txt', 'r')
# lines = file.readlines()
# for line in lines:
#     print(line, end='')
# file.close()


targetDir = "/Users/pxcm-0101-01-0128/Downloads"
# targetDir = 'd:/glt/data.txt'

# file = open(targetDir)
# for line in file:
#     print(line, end='')
# file.close()

# file = open('d:/glt/data.txt', 'w', encoding='utf-8')

for (path, subdirs, files) in os.walk(targetDir):
    print('[' + path + ']')
    # file.write(dir + '\n')
    for fname in files:
        print(os.path.join(path, fname))
        # file.write(os.path.join(dir, fname) + '\n')
