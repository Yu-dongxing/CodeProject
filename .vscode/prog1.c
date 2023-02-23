#include <stdio.h>
//函数外定义变量x和y
int x;
int y;
int addtwonum()
{
    extern int x;
    extern int y;
    x = 1;
    y = 2;
    return x+y;
}
int main()
{
    int result;
    //调用函数 addtwonum,wewrwr
    result = addtwonum();
    printf("result 为: %d",result);
    return 0;
}