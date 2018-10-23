# -*- coding:utf-8 -*-
def Feibo(n):
	if n == 1 or n == 2 :
		return 1
	else:
		return Feibo(n-2) + Feibo(n-1)

print("输入前几项？")
n = int(input())
list =[]
for i in range(1,n+1):
	list.append(Feibo(i))
print(list)