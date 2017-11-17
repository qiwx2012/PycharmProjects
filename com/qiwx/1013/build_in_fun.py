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
myslice=slice(2,10,2) #设置截取5个元素的切片
print(myslice)
arr=range(20)

for x in arr:
    print(x,end=", ")
print(" ")
bb=arr[myslice]
for y in bb:
    print(y,end=", ")

#================================
# m=divmod(1+2j,2+0.5j)
# print(m)
#========================================
print()
print('=======================')
a=[3,5,9,2]
b=sorted(a) #默认为升序
c=sorted(a,reverse=True) #True为降序排序
print(a,end=" ")
print(b,end=" ")
print(c,end=" ")
print('')
print('==============================')

l=[('b',2),('a',1),('c',3),('d',4)]
m=sorted(l,key=lambda x:x[0],reverse=True)
print(m,end=" ,")
print('')
print('==============================')
list1=[7, -8, 5, 4, 0, -2, -5]
print(sorted(list1,key=lambda x:(x<0,abs(x))),end=" ,")#x中每个元组先跟表达式比较，false排到前面，True排到后边
print('')
print('==============================')
seasons=['spring','summer','fall','winter']
l=list(enumerate(seasons,start=2))
print(l)

for i,element in enumerate(seasons):
    print(i,seasons[i])
    i+=1
print('')
print('==============================')
#k=input('input:')
# a=12
#print(type(k))
print('')
print('=============eval函数=================')
a="[[1,2],[3,2],[5,6],[9,2]]"
print(type(a))
print(a)
b=eval(a)
print(b)
print(type(b))
x=99
































