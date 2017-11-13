
for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
    print(repr(x*x*x).rjust(4))

print('{1}和{0}'.format('google','baidu'))
print('{0}和{1}'.format('google','baidu'))
print('站点列表{0},{1}和{other}'.format('google','baidu',other='taobao'))

table={'google:1','runoob:2','taobao:3'}
# for name,number in table.items:
#     print('{0:10}=>{1:10d}'.format(name,number))


class MyError(Exception):
   def __init__(self,value):
     self.value=value
   def __str__(self):
       return (self.value)

try:
    raise MyError('ooopppp')
except MyError as e:
    print('我的自定义异常信息为:',e.value)









