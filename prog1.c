#include <stdio.h>
//函数外定义变量x和y
int x;
int y;
int addtwonum()
{
    //函数内声明变量x，y为外部变量
    extern int x;
    extern int y;
    //给外部变量（全局变量）x，y赋值
    //**想给x,y一个输入环境，可以单独输入x，y的内容
    /*printf
    x=printf
                                           
                              
                                             */
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
//整数常量
//0x，0X表示16进制
//0表示8进制，不带前缀则默认表示10进制
//212         /* 合法的 */
//215u        /* 合法的 */
//0xFeeL      /* 合法的 */
//078         /* 非法的：8 不是八进制的数字 */
//032UU       /* 非法的：不能重复后缀 */

//浮点常量
//3.14159 /合法的/
//314159E-5L /合法的/js.com/make.top/23 = 
//510E /非法的，不完整的指数/
//