import  os
import sys
import io
from  urllib import request
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8') #改变标准输出的默认编码
response = request.urlopen('http://www.baidu.com/') # <http.client.HTTPResponse object at 0x00000000048BC908> HTTPResponse类型
page = response.read()
page = page.decode('utf-8')
try:
    fo = open("D:\\c.txt", mode="wb+",encoding='utf-8')
    fo.write(page)
except:
  print( "打开文件失败")
else:
  print ("打开成功")
finally:
    fo.close()
# print(page)

