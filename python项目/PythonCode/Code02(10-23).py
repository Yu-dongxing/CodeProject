# Copyright (C) 2024 YUXS, Inc. All Rights Reserved 
#
# @Time    : 2024.10.23-16:05
# @Author  : YuDongXing
# @Email   : yuxs2022@163.com
# @File    : Code02(10-23).py
#
# 1. 利用while循环输出100以内偶数的功能
def Code01():
    num = 0
    while num <= 100:
        if num % 2 == 0:
            print(num)
        num += 1


# 2. 判断用户输入的是整数还是负数的功能
def Code02():
    num = int(input("请输入一个数字："))
    if num>=0:
        print("整数")
    elif num<0:
        print("负数")
    else:
        print(f"{num}该数字错误")


# 3. 实现1-100以内逢“7”输出你的姓名的功能
def Code03():
    for i in range(1, 101):
        if i % 7 == 0 or ('7' in str(i)):
            print(f"余东兴--{i}")
        else:
            print(f"{i}")



# 4. 实现无限次猜数字功能，数字范围在1-100之间，结果会提示比设定的数字大或者小，猜中会显示猜了几次
import random
def Code04():
    i=0
    s=int(random.randint(1,100))
    while True:
        x=int(input("请输入猜的数字："))
        if x>s:
            print("猜大了")
        elif x<s:
            print("猜小了")
        elif x==s:
            print(f"恭喜你,猜对了,数字为{s},一共猜了{i}次")
            break
        i+=1


if __name__=='__main__':
    Code01()