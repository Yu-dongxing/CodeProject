/*求两数的最大公约数*/
#include <stdio.h>
int main(){
    int n1,n2,i,a;
    printf("输入两个数：");
    scanf("%d %d", &n1, &n2);
    for ( i=1; i <= n1 && i<=n2; ++i)
    {
        if (n1%i==0 && n2%i==0)
            a = i;
    }
    printf("最大公约数是：%d",a);
    return 0;    
}