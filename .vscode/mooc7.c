#include<stdio.h>
int main(){
    int k=1,s=1,i;
    scanf("%d",&k);
    for (i=0;i<k;i++)
    {
        s=(s+1)*2;
    }
    if (s<0)
    {
        printf("error");
    }
    else printf("%d",s);
    return 0;
}