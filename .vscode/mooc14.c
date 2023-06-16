/*设有一个3位数，它的百位数、十位数、个位数的立方和正好等于这个3位数，如153=1+125+27。
编写函数，返回小于等于传入参数n且满足该条件的三位数（称为水仙花数）的个数。（指定函数原型：int find(int n)）
 返回值要求：如果传入参数n不是三位数或者在该范围内没有找到，则find返回0，否则返回找到的水仙花数的个数。
 注意：不要在find函数中打印（如调用printf或puts等函数）任何数据，否则视为错误。提交的程序需要包含需要的头文件及如下的main函数：
 */
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int find(int n);
int main(){
  int n,r;
  r=scanf("%d",&n);
  if(r!=1){printf("error");return -1;}
  r=find(n);
  printf("%d",r);
  return 0;
}
int find(int n){
  int cut=0;
  if(n>=100&&n<=999)
  for(int i=123;i<n;++i){
    int a=i%10,b=i/10%10,c=i/100;
    if(a*a*a+b*b*b+c*c*c==i) cut++;
  }
  return cut;
}