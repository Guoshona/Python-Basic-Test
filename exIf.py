# -*- coding:utf-8 -*-
"""

请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖

"""
def Measure(height,weight):
	bmi = weight/float((height*height))
	return bmi

"""def Start(ans):"""
print ("请输入身高")
height = float(input ())
print ("请输入体重")
weight = float(input ())
bmi = Measure(height,weight)
if bmi< 18.5:
	print("结果：过轻")
elif (bmi >= 18.5) and (bmi < 25):
	print("结果：正常")
elif (bmi >= 25) and (bmi < 28):
	print("结果：过重")
elif (bmi >= 28) and (bmi < 32):
	print("结果：肥胖")
elif (bmi >= 32):
	print("结果：严重肥胖")
	"""print("还要计算某个人的bmi吗？")
	ans = input()
	return ans"""

"""print("计算bmi")
print("要计算某个人的bmi吗？")
ans = input()
while (ans == 'Yes'):
	Start()"""
