#!/usr/bin/python3

#import io
#import sys
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
"""
python数据类型
int(整数)
boot(布尔)
float(浮点型)
complex(复数)
"""

#流程控制
"""
if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句
"""
num = 10
if num>5:
    print("大于5")
elif num<5:
    print("小于5")


"""
循环
"""

count = 0
while count < 6:
    print(count)
    count += 1
else:
    print("count的值为",count)

