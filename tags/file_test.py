#
file = open("/Users/pxcm-0101-01-0128/Downloads/settings 2.xml", 'r')

print(file.read())
print(file.read(10))
print(file.readline())
print(file.readlines())

print(type(file.readlines()))

file.seek(0)

for line in file.readlines():
    print(line)

file.seek(0)
print(file.readline(10))
file.seek(0)
print(file.readline(10))
file.seek(0)
print(file.readline(10))
file.seek(0)
