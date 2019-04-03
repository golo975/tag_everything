#!/usr/bin/env python3
# -*- coding: utf-8 -*-

file_path = 'C:/Users/longx/OneDrive/Surge.conf'

''' 把整个文本读取为一个字符串 '''
print(open(file_path).read())
''' 读取整个文本的前N个字符串 '''
print(open(file_path).read(3))
''' 读取行的列表 '''
print(open(file_path).readlines())
''' 跨国\n读取下一行  ？？？ '''
print(open(file_path).readline())


