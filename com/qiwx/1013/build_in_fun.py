#内置函数
# dict()
a=dict(a='a',b='b',c='c')
print(a)
b=dict(zip(['one','two','three'],[1,2,3]))
print(b)
c=dict([('1',1),('2',2)])
print(c)
#===========================
it=iter([1,2,3,4,5])
while True:
    try:
        x=next(it)
        print(x)
    except:
        break
#=================================
myslice=slice(5) #设置截取5个元素的切片
print(myslice)
arr=range(10)

for x in arr:
    print(x,end=", ")
print(" ")
bb=arr[myslice]
for y in bb:
    print(y,end=", ")

