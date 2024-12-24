#include <stdio.h>

int main() {
    int num1, num2, num3;
    //输入三个整数
    printf("请输入三个整数，用空格分隔：");
    scanf("%d %d %d", &num1, &num2, &num3);
    // 使用三元运算符
    //int max = (num1 > num2) ? ((num1 > num3) ? num1 : num3) : ((num2 > num3) ? num2 : num3);
    // 输出最大值
    // 假设第一个数是最大的
    int max = num1; 
    // 比较第二个数是否比当前最大值大
    if (num2 > max) {
        max = num2;
    }
    // 比较第三个数是否比当前最大值大
    if (num3 > max) {
        max = num3;
    }
    printf("最大的数是：%d\n", max);
    return 0;
}
