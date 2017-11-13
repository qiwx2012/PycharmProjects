import socket
import sys
#创建Socket对象
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#获取本地主机名
host=socket.gethostname()
port=9999
#绑定端口
serversocket.bind((host,port))
#设置最大连接数
serversocket.listen(10)
while True:
    #建立客户端连接
      clientcocket,addr=serversocket.accept()
      print("连接地址：%s"%str(addr))
      msg='欢迎访问教程'+'\r\n'
      clientcocket.send(msg.encode('utf-8'))
      clientcocket.close()