import math
x = 10
expr = """
z = 30
sum = x + y + z
print(sum)
"""
def func():
    y = 20
    exec(expr)
    exec(expr, {'x': 1, 'y': 2})
    exec(expr, {'x': 6, 'y': 2}, {'y': 5, 'z': 4})#首先读取本地locals的值，没有再去globals里去查找
func()

def is_ood(n):
    return n%2==1
newList=filter(is_ood,[1,2,3,4,5,6,7,8,9])
for x in newList:
    print(x,end=" ")
print('\n')
def is_sqr(x):
    return math.sqrt(x) % 1 == 0
newlist = filter(is_sqr, range(1, 101))
for x in newlist:
    print(x,end=" ")
print("2的3次方在取模2:",math.pow(2,3),[3])
print("2的3次方在取模3:",pow(2,3))