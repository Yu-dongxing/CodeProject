#include<stdio.h>
int A=10;
int B=20;
char buy;
int sum,number;
int main(){
    printf ("一下是商品及价格：\n A 商品每个10：\n B 商品每个20：\n\n");
    printf ("请输入商品（A和B）：");
    scanf("%c",&buy);
    printf ("请输入数量：");
    scanf ("%d",&number);
    sum=buy=='A'?A*number:B*number;
    printf("\n你需要的%d个%c商品需要%d。\n",number,buy,sum);
    return 0;
}