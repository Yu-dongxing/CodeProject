score = float(input("请输入你的考试分数（百分制）："))

if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
else:
    grade = 'E'

print(f"你的等级制成绩是：{grade}")

#用for循环打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}",end="\t")
    print() 

# 初始列表
list = ["信息工程学院", "计算机236班", "好好学习"]

# 1. 在列表中添加姓名
list.append("李皓文")
print("添加姓名后的列表：", list)

# 2. 在下标1的位置添加一个元素“好好学习”
list.insert(1, "好好学习")
print("添加元素后的列表：", list)

# 3. 移除列表中的第一个“好好学习”
list.remove("好好学习")
print("移除第一个'好好学习'后的列表：", list)

# 4. 统计列表中所有元素的数量
count = len(list)
print("列表中元素的数量：", count)

# 5. 清空列表
list.clear()
print("清空列表后的结果：", list)
