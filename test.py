#!/usr/bin/env python3

import sys

#list = ["google" , "runoob" , "1997" , 2000]
#
#print ("人工智能 大数据")
#
#print (list)
#
#it = iter(list)  # 创建迭代器对象 可用for循环的都可迭代
#
#print (next(it)) # 输入迭代器的下一个元素
#
#
## 计算面积函数
#
#def area(width,height):
#    return width * height;
#
#def print_welcome(name):
#    return ("Welcome",name)
#
#wel = print_welcome("石清明")
#
#ar = area(5,8)
#
#print(wel,ar)



#a,b = 0,1
#
#while b < 10:
#
#   print(b)
#
#   a, b = b, a+b

#!/usr/bin/python
# -*- coding: UTF-8 -*-

## CGI处理模块
#import cgi, cgitb

## 创建 FieldStorage 的实例化
#form = cgi.FieldStorage()
#
## 获取数据
#site_name = form.getvalue('name')
#site_url  = form.getvalue('url')
#
#print "Content-type:text/html"
#print
#print "<html>"
#print "<head>"
#print "<meta charset=\"utf-8\">"
#print "<title>菜鸟教程 CGI 测试实例</title>"
#print "</head>"
#print "<body>"
#print "<h2>%s官网：%s</h2>" % (site_name, site_url)
#print "</body>"
#print "</html>"

#列表转换为字典 100

#i = ["a" , "b"]
#
#l = [1,2]
#
#print (dict([i,l]))


#打开文件 读取内容到其它 99

#with open('/Users/shiqingming/Desktop/py/test1.txt') as f1,open('/Users/shiqingming/Desktop/py/test2.txt') as f2, open('/Users/shiqingming/Desktop/py/2.txt','w') as f3:
#    for a in f1:
#        b = f2.read()
#    c = list(a+b)
#    c.sort()
#    d = ''
#    d = d.join(c)
#    f3.write(d)

#
#if __name__ == '__main__':
#    import string
#
#    fp = open('/Users/shiqingming/Desktop/py/test1.txt')
#    a = fp.read()
#    fp.close()
#
#    print (a)
#
#    fp = open('/Users/shiqingming/Desktop/py/test2.txt')
#    b = fp.read()
#    fp.close()
#
#    fp = open('/Users/shiqingming/Desktop/py/2.txt','w')
#    l = list(a + b)
#    l.sort()
#    s = ''
#    s = s.join(l)
#    fp.write(s)
#    fp.close()

#打开文件 将小写字母全部转换为大写字母 98

#if __name__ == '__main__':
#    import string
#    fp = open('/Users/shiqingming/Desktop/py/test1.txt','w')
#    string = input('please input a string:\n')
#    string = string.upper()
#    fp.write(string)
#    fp = open('/Users/shiqingming/Desktop/py/test1.txt','r')
#    print (fp.read())
#    fp.close()

#从键盘输入字符，逐个把它们写到磁盘文件上，直到输入一个#为止 97
#
#filename = input('输入文件名:\n')
#fp = open('/Users/shiqingming/Desktop/py/'+filename,'w+')
#ch = ''
#while '#' not in ch:
#    fp.write(ch)
#    ch = input('输入字符串:\n')
#fp.close()


#计算字符串中子字符串出现的次数  96

#str1 = input("请输入一个字符串:")
#str2 = input("请输入一个子字符串:")
#
#num = str1.count(str2)
#
#if num > 0:
#   print(num)
#else:
#   print(0)

#字符串日期转换为易读的日期格式  95

from dateutil import parser
dt = parser.parse('Aug 28 2015 12:00AM')
print(dt)

