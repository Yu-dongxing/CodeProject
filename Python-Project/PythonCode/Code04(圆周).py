from decimal import Decimal, getcontext #  从decimal模块导入Decimal和getcontext

def chudnovsky_pi(digits):
    getcontext().prec = digits + 1  # 设置计算精度 ，比所需位数多1位以确保准确性
    C = 426880 * Decimal(10005).sqrt() #  计算常数C，使用10005的平方根
    M = 1 #  初始化M为1
    L = 13591409 #  初始化L为13591409
    X = 1 #  初始化X为1
    K = 6 #  初始化K为6
    S = L #  初始化S为L
    for i in range(1, digits): #  循环从1到所需位数
        M = (K**3 - 16*K) * M // i**3 #  更新M的值
        L += 545140134 #  更新L的值
        X *= -262537412640768000 #  更新X的值
        S += Decimal(M * L) / X #  更新S的值
        K += 12 #  更新K的值
    pi = C / S #  计算π的值
    return +pi  # +操作符应用上下文精度 ，确保返回值符合设置的精度

digits = 10000  # 计算100位小数
print(f"丘德诺夫斯基算法计算π（{digits}位）: {chudnovsky_pi(digits)}") #  输出计算结果