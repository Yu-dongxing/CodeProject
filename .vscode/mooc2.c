/*(z-t)+(x+y)*/
#include<stdio.h>

int main()
{
    //定义变量x
    int x = 0;
    
    //输入第一次捐助希望小学x万元
    printf("请输入第一次捐助希望小学x万元");

    //调用scanf函数输入第一次捐助希望小学x万元
    scanf("%d", &x);


    //定义变量y
    int y = 0;

    //输入捐助一个癌症患者y万元
    printf("请输入捐助一个癌症患者y万元");

    //调用scanf函数输入捐助一个癌症患者y万元
    scanf("%d", &y);

    //定义变量z
    int z = 0;

    //输入举办了慈善晚会，募捐z万元
    printf("请输入举办了慈善晚会，募捐z万元");

    //调用scanf函数输入举办了慈善晚会，募捐z万元
    scanf("%d", &z);

    //定义变量t
    int t = 0;

    //输入募捐z中的t万元
    printf("请输入募捐z中的t万元");

    //调用scanf函数输入募捐z中的t万元
    scanf("%d", &t);

    //定义变量h
    int h = ( x + y)+( z - t );

    /*printf("这个明星今年一共捐助了%d元 \n ",h);*/
    printf("这个明星今年一共捐助了%d元 \n ",(x+y)+(z-t));


    return 0;

    

}