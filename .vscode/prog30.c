//输入3*4的整数矩阵中求最大值，最小值，和所有元素的平均值
#include <stdio.h>
void code1(){
    int a[3][4],max,min,i,j,*p=a[0];
    float ave=0.0;
    printf("输入3x4数组：\n");
    for(i=0;i<3;i++)
        for(j=0;j<4;j++)
            scanf("%d",p+i*4+j);
    max=min=*p;
    for(i=0;i<3;i++)
        for(j=0;j<4;j++){
            if(*(p+i*4+j)>max)max=*(p+i*4+j);
            if(*(p+i*4+j)<min)min=*(p+i*4+j);
            ave+=*(p+i*4+j);

        }
        printf("最大值是%d,最小值是%d,所有元素的平均值是%f\n",max,min,ave/12.0);
}
//用指针方法统计字符串“this is a bad we are student”中(单词)的个数
void code2(){
char s[]="this is a bad we are student",*p=s;
int n=0;
while(*p!='\0'){
    if(*p>='a'&&*p<='z'&&(*(p+1)==' '||*(p+1)=='\0'))n++;
    p++;

}
printf("单词个数是%d\n",n);
}
//输入10个整数
void code3(){
    int a[10],i,j;
    printf("输入10个整数：\n");
    for(i=0;i<10;i++){
        scanf("%d",&a[i]);
    }
    for(i=9;i>=0;i--){
        printf("%4d",a[i]);
    }
}


//
int main(){
    //code1();
    //code2();
    code3();
    return 0;
}