class TestA():
    bar=1
    def func1(self):
        print('this is fun1')
    @classmethod
    def func2(cls):
        print('this is func2')
        print(cls.bar)
        cls().func1()  #cls()为什么要加括号
TestA.func2()

def func3(arg):
    z=1
    print(locals())
func3(4)
print('\n')
a=[1,2,3]
b=[4,5,6]
c=[4,5,6,7,8]
for x in zip(a,b):
    print(x,end=" ")
print('\n')
for z in zip(b,c):
    print(z,end=" ")
print('\n')
for y in zip(*zip(a,b)):
    print(y," ")

