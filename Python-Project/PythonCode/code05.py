def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

n = 10  # 生成前10个斐波那契数
print(fibonacci_iterative(n))

def count_letters(text):
    letter_count = {}
    for char in text.lower():  # 转换为小写以忽略大小写
        if char.isalpha():  # 只统计字母
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

text = "Hello, World!"
result = count_letters(text)
print(result)


import random 
num = random.ranint(1,100)
flag = True 
while flag:
    guess_num = int(input("请输入一个1-100之间的整数："))
    if guess_num == num:
        print("恭喜你，猜对了！")
        flag = False
    elif guess_num < num:
        print("猜小了，请再试一次。")
    else:
        print("猜大了，请再试一次。")
print("游戏结束。")

i = 1
while i<=9:
    j=1
    while j<=i:
        print(f"{j} * {i} = {j * i}\t",end='')
        j+=1
    print()
    i+=1
print("乘法表打印完成。")

def Code05(n):
    # 计算n的阶乘
    if n == 0:
        return 1
    else:
        return n * Code05(n-1)

def Code06():
    #完成计算器
    while True:
        print("1.加法")
        print("2.减法")
        print("3.乘法")
        print("4.除法")
        print("5.退出")
        choice = input("请输入你的选择：")
        if choice == "5":
            break
        num1 = float(input("请输入第一个数字："))
        num2 = float(input("请输入第二个数字："))
        if choice == "1":
            print("结果：", num1 + num2)
        elif choice == "2":
            print("结果：", num1 - num2)
        elif choice == "3":
            print("结果：", num1 * num2)
        elif choice == "4":
            print("结果：", num1 / num2)
        else:
            print("无效的选择，请重新输入。")

def Code07():
    