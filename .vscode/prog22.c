#include<stdio.h>
int main(){
    double sz;
    printf("输入数字：");
    scanf("%lf",&sz);
    if (sz <= 0.0)
    {
        if (sz == 0.0)
            printf("你输入的是0");
        else
        printf("你输入的是负数");
    }
    else
    printf("你输入的是正数");
    return 0;

}
