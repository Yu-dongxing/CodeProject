/*输入一30个字符以内的字符串，判断是否为回文；如果是，则打印"true"；
否则打印"false"。像"aba"这样的从左往右读与从右往左读一致就是回文。*/
#include<stdio.h>
#include<string.h>
int main(){
    int i,l;
    char a[30];
    gets(a);
    l=strlen(a);
    for(i=0;i<=(l/2);i++){
        if(a[i]!=a[l-1-i]){
            printf("false");
            return 0;
        }
    }
    printf("true");
    return 0;
}