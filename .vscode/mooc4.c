/*判断年份是否为闰年*/
#include<stdio.h>
int main(){
    int n;
    printf("请输入1900-2200之间的年份；");

    scanf("%d",&n);

    if (n>2200||n<1900)printf ("error");

    else {if((n%400==0)||(n%4==0&&n%100!=0))

    printf("yes\n");

    else printf("no\n");
    
    }
    return 0;

}
