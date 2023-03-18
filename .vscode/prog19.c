/*十进制转换为二进制*/
/*#include<stdio.h>
#include<math.h>
long long con(int n);
int main(){
    int n;
    printf("请输入十进制数：");
    scanf("%d",&n);
    printf("十进制%d 转换为二进制为%lld",n,con(n));
    return 0;

}
long long con(int n){
    long long bin = 0;
    int remainder,i = 1,step = 1;
    while (n!=0)
    {
        remainder = n%2;
        printf("Step %d: %d/2,余数 = %d,商 =%d\n",step++,n,remainder,n/2);
        n /= 2;
        bin += remainder*i;
        i *=10;

    }
    return bin;
}*/