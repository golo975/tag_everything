#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""my test python"""

__author__ = 'gaolong'


s = 'Hello World'
print(s)

''' find() 返回字串偏移量 '''
print(s.find('Hello'))  # 0
print(s.find(' '))  # 5
print(s.find('World'))  # 6

''' replace() '''
print(s.replace('World', 'Universe'))  # Hello Universe

''' 是否是存在，返回True/False '''
print('Hello' in s)  # True

''' 去除空白'''
print(" a b ")
print(" a b ".strip())   #  'a b'   左右
print(" a b ".rstrip())  # ' a b'   右
print(" a b ".lstrip())  #  "a b "  左

''' 大小写'''
print("HELLO WORLD".lower())  # 'hello world'
print('hello world'.upper())  # 'HELLO WORLD'

''' 数字、字母 '''
print('9527'.isnumeric())  # True
print('9527'.isnumeric())  # True
print('9527'.isdigit())    # True isnumeric() 和 isdigit() 的区别待了解
print('952a'.isnumeric())  # False
print('aBc'.isalpha())     # True
print('123A'.isalpha())    # False
print('123A'.isalnum())    # True

''' 常量：小写/大写/大小写'''
import string
print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_letters)    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

''' 分割成列表'''
print('Hello, World'.split(', '))  # ['Hello', 'World']
print('Hello  World'.split())      # ['Hello', 'World']

''' 拼接列表 '''
print(''.join(['Hello', ' ', 'World']))  # 'Hello World'
print('--'.join(['Hello', 'World']))     # 'Hello--World'

''' 转换成列表 '''
print(list('Hello'))  # ['H', 'e', 'l', 'l', 'o']

''' 字符串转换为整型 '''
print(int('42'))
print(eval('42'))

''' 整型转换为字符串 '''
print(str(42))
print(repr(42))  # repr 即 representation

''' 格式化 : 下面两句是什么意思？？？？？ '''
print(("%d" % 42))
print('{:d}'.format(42))



