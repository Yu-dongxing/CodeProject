/*二进制转换为十进制*/
#include<stdlib.h>
#include<stdio.h>
#include<math.h>
int yuxs (long  n);
int main(){
    long  n;
    printf("输入二进制：");
    scanf("%lld",&n);
    printf("二进制%lld转换为十进制为：%d",n,yuxs(n));
    return 0;
}
int yuxs(long  n){
    int dec = 0,i = 0,remainder;
    while (n!=0)
    {
        remainder = n%10;
        n /= 10;
        dec += remainder*pow(2,i);
        ++i;

    }
    return dec;
    
}
