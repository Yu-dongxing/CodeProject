/*编写程序，输入一个字符串(字符串长度不超过300），
分别统计并输出该字符串中的字母个数和数字个数。
要求用指针指向这个字符串进行处理。*/
#include<stdio.h>
#define N 300
int main(){
    int i,a=0,b=0,c=0,j;
    char d[N];
    gets(d);
    for(i=0;d[i]!='\0';i++){
        if( d[i]>='a'&&d[i]<='z') a++;
        else if (d[i]>='A'&&d[i]<='Z') b++;
        else if(d[i]>='0'&&d[i]<='9') c++;
    }
    printf("字母的个数是%d,数字的个数是%d",a+b,c);
    return 0;
}