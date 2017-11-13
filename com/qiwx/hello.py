import os
import com.qiwx.modle_test
print("hello world");print("hello world");

if True:
    print("真");
else:
    print("假");


# str=raw_input("请输入： ")#输入函数
#
# print("你输入的内容是："+str)

# str = input("请输入：");
# # print ("你输入的内容是: "+str)
# print ("你输入的内容是：", str)


try:
    fo = open("D:\\a.txt", "w+")
except:
  print( "打开文件失败")
else:
  print ("打开成功")
# fo.write("www.baidu.comd你好\n")
# fo.close()

# os.rename("d:\\a.txt","d:\\b.txt")
# os.mkdir("test")

 # file=open("test","a+")


# open("test\c.txt","a+")
print(os.getcwd())
# os.removedirs("test")
a=com.qiwx.modle_test.sum(10)
print(a)













