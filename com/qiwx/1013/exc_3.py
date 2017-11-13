from urllib.request import urlopen
for line in urlopen('https://zhuanlan.zhihu.com/api/columns/zhihuadmin'):
    line=line.decode('utf-8')
    print(line)
