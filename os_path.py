#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""my test python"""

__author__ = 'gaolong'

import os
import sys

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


# targetDir = "/Users/pxcm-0101-01-0128/Downloads"
# targetDir = 'd:/glt/data.txt'
# targetDir = 'd:/'
#
# file = open(targetDir)
# for line in file:
#     print(line, end='')
# file.close()

# file = open('d:/glt/data.txt', 'w', encoding='utf-8')

# for (path, subdirs, files) in os.walk(targetDir):
#     print('[' + path + ']')
#     print(path.isalnum())
#
#     # file.write(dir + '\n')
#     # for fileName in files:
#     #     print(fileName)
#     #     print(os.path.join(path, fname))
#     #     file.write(os.path.join(dir, fname) + '\n')


current_path = os.path.realpath(".")
print(current_path)
print(os.path.basename(current_path))
print(os.path.dirname(current_path))
print(os.path.commonpath(["d:/ab/c", "d:/ab/cd"]))
print(os.path.commonprefix(["d:/ab/c", "d:/ab/cd"]))
print(os.path.exists("d:/ab"))
print(os.path.exists(current_path))

print(os.path.getctime(current_path))  # create time
print(os.path.getmtime(current_path))  # modified time
print(os.path.getatime(current_path))  # access time

print(os.path.getsize(current_path))

print(os.path.isabs(current_path))
print(os.path.isabs("."))

print(os.path.isfile(current_path))
print(os.path.isdir(current_path))

print(os.path.normcase(current_path))
print(os.path.normcase("d:/ab/cd"))



