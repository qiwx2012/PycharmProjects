#基类定义
class People:
    #定义基本属性
    name=''
    age=0
    #定义私有属性
    __weight=0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.w=w
    def speak(self):
        print("%s say:I am %d years old."%(self.name,self.age))

class ChildPeople(People):
    def say(self):
        print(self.speak())

child=ChildPeople('小红',10,110)
child.speak()


class Student:
    '一个简单的示例'
    studentId=1001
    studentName="小明"
    def f(self):
        return 'hello student'
    def modefyName(self,x):
        self.studentName=x

#实例化对象
x=Student()
print('Student的属性 studentId：',Student.studentId)
print('Student的属性 studentName：',Student.studentName)
print('Student的方法输出:',x.f())
print('Student的实例 studentName：',x.studentName)
x.modefyName('张明')
print('Student的实例 studentName：',x.studentName)
print('Student的属性 studentName：',Student.studentName)