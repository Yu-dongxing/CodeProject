#include<stdio.h>
int main(){
    double a,b,c;
    printf("输入第一个：");
    scanf("%lf",&a);
    printf("2个:");
    scanf("%lf",&b);
    c=a;
    a=b;
    b=a;
    printf("%.2lf\n",a);
    printf("%.2lf",b);
    return 0;
}