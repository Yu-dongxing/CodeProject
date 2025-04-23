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