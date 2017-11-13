def hello():
    print("hello wrold!")

hello()
#计算面积
def area(width,height):
    return width*height
w,h=4,5
print('width=%d,height=%d,area=%d'%(w,h,area(w,h)))

def modify(b):
    b.append(5)
a=[1,3,4]
print(a)
modify(a)
print(a)

sum= lambda arg1,arg2:arg1+arg2;
print(sum(22,44))
if True:
    message="你好啊"
def sum(a,b):
    total=a+b
    print("内函数：",total)
    return total
total=sum(10,20)
print("函数外:",total)

print(message)




