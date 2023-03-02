/*求一元二次方程：ax2+bx+c=0 的根。
输入三个实数a,b,c的值，且a不等于0。*/
/*#include<stdio,h>
#include<math.h>
int main(){
    float a,b,c,x1,x2,d;
    scanf("%f %f %f",&a,&b,&c);
    if(a!=0){/*检查两个操作数的值是否相等，如果不相等则条件为真
        d=sqart(b*b-4*a*c);
        x1=(-b+b)

    }

}*/
#include<stdio.h>
int main(){
    int var = 20;
    int *ip;
    ip = &var;
    printf("var的地址:%p\n",&var );
    printf("ip存储地址:%p\n",ip);
    printf("ip的值：%d\n",*ip);
    return 0;
}