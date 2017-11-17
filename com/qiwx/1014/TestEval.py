x=1
y=6
num1=eval('x+y')
print("num1:",num1)
dict={'x':11,'y':22}
def g():
    x=2
    y=2
    num2=eval('x+y')
    print("num2:",num2)
    num3=eval('x+y',locals=locals())#取的是局部x和y的值
    print("num3:",num3)
    num3=eval('x+y',dict)#取的是全局x和y的值
    print("num3:", num3)
    # print(locals()['x'])
    # print(locals()['y'])
    # print(globals()['x'])
    # print(globals()['y'])
g()
print(globals()['x'])
print(globals()['y'])
print(locals()['x'])
print(locals()['y'])

