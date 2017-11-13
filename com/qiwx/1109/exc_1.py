content = input('请输入你家狗的年龄：')
print('')


# while(not content.isnumeric()):
while not content.isnumeric():
    content = input('请输入正确的年龄：')
    # print('')
age=int(content)
if age < 0:
    print("你是在逗我么?")
elif age == 1:
    print("相当于14岁的人")
elif age == 2:
    print("相当于22岁的人")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄：", human)
    ###退出提示
input("点击enter键退出")