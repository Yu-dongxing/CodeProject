/*#include<stdio.h>
#include<stdlib.h>
/*int main(){
    int n,r;
    long result=1;
    r = scanf("%d",&n);
    if (r<1)
    {
        printf("input error");
        return -1;
    }
    for (int i = 1;i <=5;++i)
    {
        result *= n;
        printf("%ld",result);
    }
    printf("\n");
    system("pause");
    return 0;
}*/

/*int main(){
    int i,j;
    for (i=1;i<10;i++)
    printf(" %4d ",i);
    printf("\n------------------------\n");
    for (i=1;i<10;i++)
     for(j=1;j<10;j++)
      if (j!=9)
        printf("%4d",i*j);
      else
        printf("%4d\n",i*j);
   return 0;
      
}*/

/*#include<stdio.h>
int main(){
    double m = 0.8,msum = 0;
    int n = 2,sum = 0,i;
    for (i = 1;n<100; ++i)
    {
        sum += n;
        n*=2;
    }
    msum = (sum*m)/(i-1);
    printf("明天开销%.2f\n",msum);
    return 0;
}*/

/*#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int main(){
    int magic;
    int guess;
    int counter;
    srand(time(NULL));
    magic= rand()%100+1;
    counter = 0;
    do
    {
        printf("请输入数字:");
        scanf("%d",&guess);
        counter ++;
    if (guess>magic)
    {
        printf("错误，高了\n");
    }
    else if (guess<magic)
    {
        printf("错误，底了\n");
    }
    else{
        printf("正确\n");
        printf("这个数字是%d\n",magic);
    }
    } while (guess != magic && counter<10); 
    printf("次数为%d\n",counter);
    system("pause");
    return 0;
}*/


/*
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main(){
    int n,i,b=1,r;
    printf("输入数字n：");
    r=scanf("%d",&n);
    if (r<1)
    {
        printf("错误的素数\n");
        return -1;
    }
    for (i = 2;i <= sqrt(float(n));++i)
    {
        if (n%i == 0)
        {
            b = 0;break;
        }
    }
    if (b == 0)
    printf("%d不是素数\n",n);
    else printf("%d是素数\n",n);
    return 0;
}*/


/*#include<stdio.h>
#include<math.h>
int main(){
    int a[10]={0};
    scanf("%d",&a[2]);
    scanf("%d",&a[3]);
    printf("%d,%d",a[2],a[3]);
    return 0;
}*/



/*#include<stdio.h>
#include<stdlib.h>
int main(){
    int n=10,m=0,i;
    float a[n],ms = 0;
    for (i = 0; i < n;++i)
    scanf("%f",&a[i]);
    for ( i = 0; i<n;++i)
        if (ms<a[i])
        {
            ms = a[i];
            m = i;
        }
        printf("ms %.2f\nm %d\n",ms,m);
        return 0;
        
}*/



/*#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(){
    const int n=20,m=5;
    char name[][n] = {
        "kata.wate","james.yu","bull.ss","jimes.rt"
    };
    char james[]  = "james";
    int i,l,len=strlen("james");
    for (i = 0;i<m;++i)
    {
        for (i = 0;i<len;++i)
        {
            if (name[i][l]!= james[l])break;
        }
        if (i==len)
        
        printf("%s has james\n",name[i]);
    }
    return 0;
}*/




/*a=5,b=3,c=1//100==100abc/*/
/*#include<stdio.h>
#include<stdlib.h>
int main(){
    int a,b,c;
    for (a=0;a<=20;a++)
    {
        for (b=0;b<=33;b++)
        {
            c=((100-(5*a+3*b))*3);
            if (a+b+c==100)
            printf("%d,%d,%d\n",a,b,c);
        }
    }
    return 0;
}*/



/*#include<stdio.h>
int main(){
    double x;
    scanf("%lf",&x);
    if (x<=50)
    printf("%.2lf",1.9*x);
        else if (x<=200)
            printf("%.2lf",2.8*x);
                else if(x>200)
                    printf("%.2lf",3.7*x);
    return 0;
}*/



/*
#include<stdio.h>
#include<stdlib.h>
const int n =4,m = 20;
typedef struct stuent {
    char name [m];
    int id;
    float chinese;
    float english;
    float math;

}student;
int  main(){
    student s[n],tmp;
    int i,max,j;
    for (i = 0;i<n;++i)
    printf("姓名：");
    scanf("%s",&s[i].name);
    printf("ID:");
    scanf("%d",&s[i].id);
    
    scanf("%s%d%f%f%f",&s[i].name,&s[i].id, &s[i].chinese,&s[i].english,&s[i].math,n-1);

for (i = 0;i<n;++i){
    max = i;
    for (j = i+1;j<n;++i);
    if (s[i].chinese>s[max].chinese)max =j;
    tmp = s[i];
    s[i]=s[max];
    s[max]= tmp;

}
for (i = 0;i<n;++i)
    printf("%s %d %.2f %.2f %.2f\n",s[i].name,s[i].id,s[i].chinese,s[i].english,s[i].math);
}*/



/*
#include <stdio.h>
#include <math.h>
/*爱心代码
int main()
{
    int x, y;
    double d;
    for (y = 30; y >= -30; y--)
    {
        for (x = -30; x <= 30; x++)
        {
            d = pow(pow(x * 0.04, 2) + pow(y * 0.1, 2) - 1, 3) - pow(x * 0.04, 2) * pow(y * 0.1, 3);
            putchar(d <= 0.0 ? '*' : ' ');
        }
        putchar('\n');
    }
    return 0;
}*/
/*
#include<stdio.h>
int main(){
    int a[10]={0,2,4,6,8,10,12,14,16,18};
    int sum = 0;
    int *b = a;
    for (int i=0;i<10;i++)
    {
        sum=sum+*b;/* sum+=*b */ /*
        *b++;
    }
    printf("sum is %d\n",sum);
    return 0;
}*/
/**
#include<stdio.h>
int main(){
char a[]="rtretee";
char *p=a,**c;

printf("%s",c);
return 0;
}**/
/**
#include<stdlib.h>
#include<stdio.h>
int main(){
    int *p=NULL,n,i;
    double aver,sum;
    printf("输入：");
    scanf("%d",&n);
    p = (int *) malloc(n*sizeof(int));
    if(p==NULL){
        printf("error\n");
        exit(1);

    }
    printf("输入s；");
    for(i=0;i<n;++i){
        scanf("%d",&p[i]);
        sum+=p[i];

    }
    aver=sum/n;
    printf("aver=%.1f\n",aver);
    free(p);

}
**/

/**
#include<stdio.h>
void s1(int a,int b);
int main(){
    int a=3,b=4;
    printf("a=%d,b=%d\n",a,b);
    s1(a,b);
    return 0;

}
void s1(int a,int b){
    int c;
    c=a;
    a=b;
    b=c;
    printf("a=%d,b=%d\n",a,b);

}
**/
/**
#include<stdio.h>
void s1( char a1[],char a2[]){
    int i,j;
    for(i=0;a1[i]!='\0';i++);
        for(j=0;a2[j]!='\0';j++)
        a1[i+j]=a2[j];
    a1[i+j]='\0';
}
int main(){
    char a1[100],a2[100];
    printf("输入a1：");
    gets(a1);
    printf("输入a2:");
    gets(a2);
    s1(a1,a2);
    printf("%s\n",a1);
    return 0;

}
**/

/**
#include<stdio.h>
int csjg=100;
void sp1();
void sp2();
void sp3();
void xg();
int main(){
    printf("原价格：%d\n",csjg);
    sp1();
    sp2();
    sp3();
    xg();
    printf("修改的价格是：%d\n",csjg);
    sp1();
    sp2();
    sp3();
    return 0;
}
void sp1(){
    printf("一号价格为；%d\n",csjg);

}
void sp2(){
    printf("2号价格为：%d\n",csjg);

}
void sp3(){
    printf("3号价格为：%d\n",csjg);

}
void xg(){
    printf("请修改价格：");
    scanf("%d",&csjg);

}
**/
/**
#include<stdio.h>
#include<stdlib.h>
int s1();
int a;
int s1(){
    scanf("%d",&a);
}
int main(){
    s1();
    printf("%d\n",a);
}
**/
/**
#include<stdio.h>
void s1(int a,int b,int c){
    float a1=0,b1=0,c1=0;
    a1=(float)180*a/(a+b+c);
    b1=(float)180*b/(a+b+c);
    c1=(float)180*c/(a+b+c);
    printf("度数为：%.1f,%.1f,%.1f",a1,b1,c1);

}
int main(){
    s1(2,3,3);
    return 0;
}

**/
/**#include<stdio.h>
#include<stdlib.h>
#define N 10
int main(){
    int *p,*q,i=0;
    q=p=(int *)malloc(N*sizeof(int));
    if(p){
        for(i=0;i<N;++i,++p){
            *p=i+1;
            printf("%d",*p);
        }
        free(q);
        return 0;
    }
}**/
/*字符串的拷贝（40分）
编程实现函数：void my_strcpy(char * destination,char * source);
函数功能：将source指向的字符串拷贝到destination指向的位置。
注意：使用空格字符来表示字符串的结束。
例如source指向的空间，依次保存了字符'a'，字符'b'，字符空格' '，字符'c'，
则source指向的字符串为"ab c"。destionation原来存储的字符串是"xyz tdk"，
则拷贝后，source字符串的内容不变，destionation存储的字符串修改为“ab  tdk”。
遇到异常情况，输出"error"；否则不要随意输出，会视为错误.
您的main函数需要读入2个长度不超过80字节的字符串(按行依次读入source和destionation字符串），
然后调用my_strcpy函数，最后用puts函数输出destionation里面存储的字符串。
例如：
输入1：xyz abc a kp
输出1:xyz
输入2：xyz abc a kppp
输出2：xyz pp
提示：注意这里传入的字符串保证是有空格的，所以是以空格作为字符串结束，而不是实际是字符串结束符。
*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define N 80
void my_strcpy(char * destination,char * source);
int main(){
    char source[N],destination[N];
    gets(source);
    gets(destination);
    my_strcpy(destination,source);
    puts(destination);
    return 0;
}
void my_strcpy(char * destination,char * source){
    int i=0;
    while(source[i]!=' '&&source[i]!='\0'){
        destination[i]=source[i];
        i++;
    }
    destination[i]='\0';
    if(source[i]=='\0'){
        return;
    }
    else{
        my_strcpy(destination+i+1,source+i+1);
    }
}