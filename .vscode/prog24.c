#include<stdio.h>
#include<stdlib.h>
/*int main(){
    int n,r;
    long result=1;
    r = scanf("%d",&n);
    if (r<1)
    {
        printf("input error");
        return -1;
    }
    for (int i = 1;i <=5;++i)
    {
        result *= n;
        printf("%ld",result);
    }
    printf("\n");
    system("pause");
    return 0;
}*/
int main(){
    int i,j;
    for (i=1;i<10;i++)
    printf(" %4d ",i);
    printf("\n------------------------\n");
    for (i=1;i<10;i++)
     for(j=1;j<10;j++)
      if (j!=9)
        printf("%4d",i*j);
      else
        printf("%4d\n",i*j);
   return 0;
      
}