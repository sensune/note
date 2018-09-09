import time
d = 'd'
def timmer(f):  #装饰器函数
    def inner(*args,**kwargs):
        start = time.time()
        re = f(*args,**kwargs)
        end = time.time()
        print(end - start)
        return re
    return inner
@timmer #语法糖 @装饰器函数名 相当于func = timemer(func)
def func(a,b,c):
    print("被装饰的函数")
    print(a,b,c)

#func = timmer(func)
func('参数a','参数b',c = '参数c')
