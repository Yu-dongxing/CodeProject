/*功能：
实现删除字符串中连续的重复字符（除字母和数字）。
 输入为字符串，将字符串中连续重复的，非字母和数字的字符重复的删去，然后输出处理后的字符串。
 要求用指针指向输入的字符串进行操作。*/
#include<stdio.h>
#include<string.h>
#include<math.h>
int main(){
    int i,b,c,*d,e,f;
    char a[10];
    printf("输入：");
    scanf("%s",&a);
    for(i=0;i< '\0';i++){
            if(a[i]==a[i-1]){
            continue;
            } 
            puts(a);
    }
    
    return 0;
}
