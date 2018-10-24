# -*- coding:utf-8 -*-
from functools import reduce
'''
利用map()函数，把用户输入的不规范的英文名字，
变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，
输出：['Adam', 'Lisa', 'Bart']：
'''
print ("第一题结果")
list1 = ['adam','LISA','barT']
def xLower (x):
	return x.lower()
def xCapitalize (x):
	return x.capitalize()
	
list2 = list(map(xLower,list1))	
list3 = list(map(xCapitalize,list2))	
print (list3)

'''
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
'''
print ("第二题结果")
def prod(x,y):
	return x*y
listno2 = [2,15,58,2,77,9,3]
listno21 = reduce(prod,listno2)
print(listno21)
print ("第三题结果")
'''
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
'''

str = '123.4567'
def str2float(str):
	def fn(x,y):
		return x*10+y
	n = str.index('.')
	s1 = list (map(int,[x for x in str[:n] ]))
	s2 = list (map(int,[x for x in str[n+1:]]))
	return reduce(fn,s1)+reduce(fn,s2)/10**len(s2)
newPrint = (str2float(str))
print (newPrint)
