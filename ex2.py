# -*- coding:utf-8 -*-
#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
before = 72
now = 85
improve = (now-before)/now * 100 
print ('%1f%%' % improve)