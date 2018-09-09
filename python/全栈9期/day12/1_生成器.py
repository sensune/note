#/usr/bin/env python3

#生成器函数(含有yield关键字)
#yield和return关键字不能同时存在
def generator():
    print(1)
    a = 123
    yield 'a'
    print(2)
    

g = generator()
#print(g.__next__())
print(next(g))
