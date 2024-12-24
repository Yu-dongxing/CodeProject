#include <stdio.h>

// int main()
// {
//     printf("Please display these words: \n" );
//     printf("1. press return keyboard to enter the game. \n");
//     printf("2. press esc keyboard to exist the game. ");
//     return 0;
// }
// #include <stdio.h>
//输入字符串，找到IT，返回个数


int main()
{
	char str[81];
	int i,c;        /*变量c存放个数*/
	gets(str);      /*$BLANK$*/
    c=0;            /*$BLANK$*/   
	i=1; 
	while(str[i]!='\0')
	{
		if (str[i-1]=='I'&&str[i]=='T')
            c++;
            i++;
	}
	printf("%d\n",c);
	return 0;
}