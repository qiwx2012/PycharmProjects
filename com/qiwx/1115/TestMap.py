def square(x):
    return x*2
a=map(square,[1,2,3,4])
for x in a:
    print(x,end=" ")
print("\n")
b=map(lambda x:(x**2)+10,[1,2,3,4]) #平方加10
for y in b:
    print(y,end=" ")
print('\n')
c=map(lambda x,y:x+y,[1,2,3,4,5],[1,2,3,4,10]) # 提供了两个列表，对相同位置的列表数据进行相加
for y in c:
    print(y,end=" ")
print('\n')
__import__('com.qiwx.1110.AAA')
pH=12
ph=11
print(pH,ph)


