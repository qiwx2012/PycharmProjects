import  sys
def fibonacci(n):
    a,b,counter=0,1,0
    while True:
        if(counter>n):
            return
        yield a
        # a=b
        # b=a+b
        a,b=b,a+b  #此行代码等价于以下代码
        print("a=%d,b=%d"%(a,b))
        counter+=1
f=fibonacci(10)
while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()

