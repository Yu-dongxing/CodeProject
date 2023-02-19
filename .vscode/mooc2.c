/*(z-t)+(x+y)*/
#include<stdio.h>
int main()
{
    int x = 0;
    
    printf("请输入第一次捐助希望小学x万元");

    scanf("%d", &x);

    int y = 0;

    printf("请输入捐助一个癌症患者y万元");

    scanf("%d", &y);

    int z = 0;

    printf("请输入举办了慈善晚会，募捐z万元");

    scanf("%d", &z);

    int t = 0;

    printf("请输入募捐z中的t万元");

    scanf("%d", &t);

    int h = ( x + y)+( z - t );

    printf("这个明星今年一共捐助了%d元 \n ",h);

    return 0;

    

}


