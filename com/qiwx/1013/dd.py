students = [('john', 'A', 15), ('jane', 'B', 12), ('dave','B', 10)]
sorted(students,key=lambda s: x[2]) #按照年龄来排序
print(students,end=" ,")