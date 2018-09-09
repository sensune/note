name = "sensune"
psw = "123456"
i = 3
while i>0:
    in_name = input("请输入用户名：")
    in_psw = input("请输入密码：")
    if in_name == name and in_psw == psw:
        print("登录成功")
        break
    else:
        if(i == 1):
            print("你已经输入错误3次")
            break
        else:
            print("登录失败，请重新输入用户名和密码,剩余次数:",i-1)
            i -= 1
