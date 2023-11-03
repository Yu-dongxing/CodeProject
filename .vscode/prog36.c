#include<stdio.h>
// （code1） ：喜欢你循环代码
void code1(){
    int line = 0;
    while(line<1000){
        printf("xhn %d\n",line);
        line++;

    }
    if(line>=1000)printf("wyxhn\n");
}
void code2(){
    int a[8]={2,4,6,1,3,7,8,1};
    int b[8]={6,5,3,8,6,4,7,5};
    for(int i=0;i<8;i++){
        for(int j=0;j<8;j++){
            printf("%d:::%d",a[i],b[j]);
            if(j%8==0)printf("\n");
        }
    }
    for(int i=0;i<10;i++){
        printf("——");
    }
}
void code3(){
    /*从键盘任意输入三个整数，将它们按从小到大的顺序输出（要求使用选择结构实现）。*/
    int a,b,c,t;
    scanf("%d%d%d",&a,&b,&c);
    if(a>b)
    {
		t=a;
		a=b;
		b=t;
    }
    if(a>c)
    {
		t=a;
		a=c;
		c=a;
    }
    if(b>c)
    {
		t=b;
		b=c;
		c=t;
    }
    printf("%d\t%d\t%d\n",a,b,c);
}
void code4(){
    /*根据下式计算s的值，其中n由键盘输入。
    说明：(1)要求使用循环实现；(2)输出结果保留4位小数，形式为：s=1.2345
    参考答案：参考运行结果： 输入：2000输出：s=1.5706*/
    int i,n;
    double s=1;
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
		s=s*(2*i)*(2*i)/((2*i-1)*(2*i+1));
    }
    printf("s=%.4f\n",s);
}
void code5(){
/*某购物中心根据顾客购买商品的总金额（单位：元）进行打折促销，
        输入顾客购买商品的总金额x（设x是大于0的整数），
        计算并输出顾客应付总金额y（要求使用选择结构实现）。*/
    int x;
    scanf("%d",&x);
    if(x<100){
        printf("%d",x);
    }else if(x>=100&&x<200){
        printf("%d",0.95*x);
    }else if(x>=200&&x<400){
        printf("%d",0.9*x);
    }else if(x>=400){
        printf("%d",0.85*x);
    }
}
void code6(){
    	int n=1;
	double s=0,t;
	while(s<=4)
	{
		t=1.0/(2*n-1);
		s=s+t;
		n++;
	}
	printf("n=%d\n",n-1);
}
void code7(){
/*题目：小明每天坚持跑步，6月份每天的跑步里程（单位：千米）记录在数组a中。计算并输出小明6月份跑步总里程和每天平均值（要求使用循环实现，结果保留2位小数）。
输出格式为：小明6月份跑步总里程：123.45千米平均值：12.34千米
参考答案：参考运行结果：小明6月份跑步总里程：324.91千米 平均值：10.83千米*/
/*小明6月份每天跑步里程*/
	double a[30]={10.25,8.79,9.54,12.1,16.8,10.3,8.98,9.78,11.26,12.9,10.75,8.77,8.54,10.31,13.8,12.3,8.57,9.43,10.28,11.3,11.47,9.49,10.54,11.61,13.85,12.73,8.28,9.87,10.6,11.72}; 
	/*考生在此行下设计程序，不得删除本行*/
	double total=0,aver;
	int i;
	for(i=0;i<30;i++)
		total+=a[i];
	aver=total/30;
	printf("小明6月份跑步总里程：%.2lf千米\n平均值：%.2lf千米\n",total,aver);
}
// 
int main(){
    code2();
    return 0;
}