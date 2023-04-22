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

#include<stdio.h>
int main(){
    int a[10]={0,2,4,6,8,10,12,14,16,18};
    int sum = 0;
    int *b = a;
    for (int i=0;i<10;i++)
    {
        sum=sum+*b;/* sum+=*b */
        *b++;
    }
    printf("sum is %d\n",sum);
    return 0;
}

