/*编写程序，从键盘输入5个正整数，然后通过多次调用LCM（LCM功能：
对两个正整数求最小公倍数），求出这5个数的最小公倍数，并输出该值。
其中最小公倍数函数原型：int LCM(int x, int y) 返回值为x和y的最小公倍数
如果输入数据错误，输出"error"。*/
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int LCM(int x,int y){
    int z;
    z=x*y/fabs(x-y);
    return z;
}
int main(){
    int a[5],i,j,k,lcm;
    printf("请输入5个正整数：");
    for(i=0;i<5;i++){
        scanf("%d",&a[i]);
    }
    lcm=a[0];
    for(i=1;i<5;i++){
        lcm=LCM(lcm,a[i]);
    }
    printf("最小公倍数为：%d",lcm);
    return 0;
}
