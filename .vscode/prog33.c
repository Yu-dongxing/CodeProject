//位运算章节
//1  ~ 取反运算  一元（目）运算符
//2  & 按位与运算 二元（目）运算符
//3  | 按位或运算 二元（目）运算符
//4  ^ 按位异或运算 二元（目）运算符
#include<stdio.h>
#define N 200
//code1和code2为   ~ 取反运算
//规则为对二进制数按位取反，00010101变为11101010
void code1(){
    char x[N]={"1 ~ 取反运算  一元（目）运算符"};
    int a=45,b;
    b=~a;

    printf("%o,%o",a,b);//%o 以8进制形式输出无符号整数（不输出前导符0）
}

void code2(){
    int a=-32,b;
    b=~a;
    printf("%o,%o",a,b);
}
//按位与运算（code3）
//规则是  0&0=0 1&0=0 0&1=0 1&1=1
void code3(){
    //将整形变量a的高字节清0，保留低字节数据
    int a=14728;
    a=a&0x00ff;
    printf("%d\n",a);

}
//按位或运算
//规则为  0|0=0，1|0=1，0|1=1，1|1=1
void code4(){
    int a=14728;
    a=a|0x00ff;
    printf("%o\n",a);
}


int main(){
    int a;
    printf("1  ~ 取反运算  一元（目）运算符\n");
    printf("2  & 按位与运算 二元（目）运算\n");
    printf("3  | 按位或运算 二元（目）运算符\n");
    printf("4  ^ 按位异或运算 二元（目）运算符\n");
    printf("输入示例代码序号：");
    scanf("%d",&a);
    switch (a)
    {
    case 1:code1();break;
    case 2:code2();break;
    case 3:code3();break;
    case 4:code4();break;
    //case 5:code5();break;
    //case 6:code6();break;
    default:printf("序号错误");break;
    }
    return 0;
}