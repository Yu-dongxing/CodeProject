/*功能：
实现删除字符串中连续的重复字符（除字母和数字）。
 输入为字符串，将字符串中连续重复的，非字母和数字的字符重复的删去，然后输出处理后的字符串。
 要求用指针指向输入的字符串进行操作。*/
#include<stdio.h>
#include<string.h>
#include<math.h>
#define N 302
int main(){
    int i,b,c,*d,e,f;
    char a[N];
    *d=a[N];
    printf("输入：");
    scanf("%s",&*d);
    for(i=0;a[i]!='\0';i++){
            if(d==d-1){
            continue;
            }
        printf("%c",a[i]);
    }
    return 0;
}
