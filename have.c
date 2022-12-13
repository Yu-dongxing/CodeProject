#include <stdio.h>
 int main()
 {
    /*变量定义*/
    /*<类型名称》《变量名称》
      int price 
      int amount
       int price ,amount 
             c的保留字
                auto,break,case,cher,const,continue,default */
    int price = 0;/*定义一个变量，名字是price ，类型是int，初始值是0*/
 
    printf("请输入商品金额（元）");

    scanf("%d", &price);

    int amount = 0;

    printf("请输入给定的总金额（元）");

    scanf("%d", &amount);

    int change = amount - price;

    printf("找你%d元。 \n",change);

    return 0;
 }