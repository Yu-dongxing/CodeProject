/*接受若干非负整数（数据不重复），当个数超过10个或者遇到负数时停止接受，
将这几个正整数按升序排列输出，并且奇数在前，偶数在后。*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main (){
    int a[10],i,j,x,k=0,len=0;
    for(i=0;i<10;i++){
        x=scanf("%d",&a[i]);
        if(a[i]<0||x==0)break;
        len++;
    }
    for(i=0;i<len-1;i++){
        for(j=0;j<len-1-i;j++){
            if(a[j] % 2==0){
                k=a[j];
                a[j]=a[j+1];
                a[j+1]=k;

            }
        }
    }
    for(i=0;i<len-1;i++){
        for(j=0;j<len-1-i;j++){
            if(a[j]>a[j+1]&&a[j]%2&&a[j+1]%2){
                k=a[j];
                a[j]=a[j+1];
                a[j+1]=k;

            }
        }
    }
    for(i=0;i<len-1;i++){
        for(j=0;j<len-1-i;j++){
            if(a[j]>a[j+1]&&a[j]%2==0&&a[j+1]%2==0){
                k=a[j];
                a[j]=a[j+1];
                a[j+1]=k;

            }
        }
    }
    for(i=0;i<len;i++){
        printf("%d ",a[i]);

    }
    printf("\n");
    return 0;

}