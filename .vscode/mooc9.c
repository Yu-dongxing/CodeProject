/*
书有书名(字符串长度不超过50字节)，价格（单精度实数），分类（正整数）。
书的结构定义如下:
struct book
{
	char name[50];
	float price;
	int classification;	
}; 
输入n本书（n<=100)，及每本书的书名，价格和分类(空格分隔输入数据)， 
请分别根据价格递增顺序排序，如果价格相同，则按照书名(ASCII码）递增排序。
最后输出排序后的结果，每行一本书详细信息，按照：书名，价格(保留2位小数），分类由逗号分隔。
*/
#include<stdio.h>
#include<string.h>
struct books {
	char name[50];
	float price;
	int classf;
}book;
int main(){
	int i,n,j;
	scanf("%d",&n);
	for(i=0;i<n;i++){


	}
	return 0;
	
}