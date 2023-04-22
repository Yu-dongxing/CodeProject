/*#include<stdio.h>
int main(){
    int  a,c,u;
    int *b,*d,*e;
    b = &a;
    d = &c;
    e = &u;
    scanf("%d,%d",&a,&c);
    if (a<c){
        *e = *d;
        *d = *b;
        *b = *e;
    }
    printf("a:%d,b:%d",*b,*d);
    return 0;
}*/
#include<stdio.h>
#include<windows.h>			//控制dos界面
int color(int c)
{
	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), c);        //更改文字颜色
	return 0;
}
int main()
{
	int hour = 0, min = 0, sec = 0;
	int i, j, k;
	printf("请输入倒计时时间（例如：01:26:30）：");
	scanf("%d:%d:%d", &hour, &min, &sec);
	if (hour > 24 || hour < 0 || min>60 || min < 0 || sec>60 || sec < 0) {

		printf("输入有误！\n");
		return 0;
	}
   color(12);
	printf("\n       倒计时软件\n");
   color(10);
	printf("     ===============\n");
	color(1);
	for (i = hour; i >= 0; i--) 
	{
		for (j = min; j >= 0; j--)
		{
			for (k = sec; k >= 0; k--) 
			{
				printf("\r        %2d:%2d:%2d", i, j, k);
				Sleep(1000);
			}
			sec = 59;
		}
		min = 59;
	}
	exit(0);
	return 0;
}