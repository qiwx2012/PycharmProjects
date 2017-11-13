import os
import math
student={'tom','jim','mary'}
if('tom1'  in student):
    print('tom1'+'在集合里')
else:
    print('tom'+'不在集合中')

a=60
b=13

print(a&b)
print(math.sqrt(16))

str=""""
这事一个多行字符串例子
TAB（\t）。
也sky使用换行符[\n]。
"""
print(str);

str1='''这事一个多行字符串例子
TAB（\t）。
也sky使用换行符[\n]。'''
print(str1);

a="fdsfdf"
print(a.center(20,"-"))
print(a.upper())
list=[12,33]
print(list)
list.append('cc')
print(list)
for x in [1, 2, 3]: print(x, end=" ")



citys={
    '北京':{
        '朝阳':['国贸','CBD','天阶','我爱我家','链接地产'],
        '海淀':['圆明园','苏州街','中关村','北京大学'],
        '昌平':['沙河','南口','小汤山',],
        '怀柔':['桃花','梅花','大山'],
        '密云':['密云A','密云B','密云C']
    },
    '河北':{
        '石家庄':['石家庄A','石家庄B','石家庄C','石家庄D','石家庄E'],
        '张家口':['张家口A','张家口B','张家口C'],
        '承德':['承德A','承德B','承德C','承德D']
    }
}

for i in citys['北京']['海淀']:
    print(i)


def sum():
    print(citys)





