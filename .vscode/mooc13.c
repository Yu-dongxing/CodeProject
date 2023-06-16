/*编写程序，输入两个字符串，通过2个指针p和q分别指向这2个字符串，
比较字符串是否相等。 要求不使用strcmp函数。*/
#include<stdio.h>
#include<string.h>
#define N 256
int main(){
    int i,j,a,b,c;
    char d1[N],d2[N];
    printf("输入d1；");
    gets(d1);
    printf("输入d2；");
    gets(d2);
    for (i=0;d1[i]!='\0';i++){
            if(d1[i]==d2[i]) a=0;
            else if(d1[i]!=d2[i]) a=1;
    }
    if(a==0)printf("equal\n");
    else if(a==1)printf("unequal\n");
    return 0;
}
