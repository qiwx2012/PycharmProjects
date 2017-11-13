import  sys
# n=100
# sum=0
# count=1
# while count<=n:
#  sum=sum+count
#  count+=1
# print("1到%d之和为%d"%(n,sum))
# #while 循环使用else语句
# count=0
# while count<5:
#  print(count,"小于5")
#  count=count+1
# else:
#  print(count,"大于或等于5")
#while 使用Break跳出循环
sites=['baidu','google','souhu','sina']
for site in sites:
  if site=='souhu':
      print('souhu 不需要继续执行了')
      break
  print(site)
else:
   print('没有循环数据')
print('完成循环')

for i in range(5):
    print(i)
print(3,4,5)

try:
    print(11)
except StopIteration:
    sys.exit()