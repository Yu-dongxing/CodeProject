#include <stdio.h>
 int main()
 {
    int price = 0;
 
    printf("请输入商品金额（元）");

    scanf("%d", &price);

    int amount = 0;

    printf("请输入给定的总金额（元）");

    scanf("%d", &amount);

    int change = amount - price;

    printf("找你%d元。 \n",change);

    return 0;
 }