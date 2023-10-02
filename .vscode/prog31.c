//结构体 输入3个学生的信息后输出，信息包括学号，姓名，和4个课程的成绩
#include <stdio.h>
//代码1
int code1(){
    struct student{
        char name[20];
        int num;
        float score[4];
    }student[3];
    
    int i,j;
    float t;
    printf("请输入3个学生的信息(学号，姓名，4个成绩):\n");
    for(i=0;i<3;i++){
        scanf("%d",&student[i].num);
        scanf("%s",&student[i].name);
        for(j=0;j<4;j++){
            scanf("%f",&t);
            student[i].score[j]=t;
        }
    }
    printf("学号\t姓名\t成绩1\t成绩2\t成绩3\t成绩4\n");
    for(i=0;i<3;i++){
        printf("%ld %s\t",student[i].num,student[i].name);
        for(j=0;j<4;j++){
            printf("%.1f\t",student[i].score[j]);
        }
        printf("\n");
    }
    return 0;
}
//代码2
//有五个学生，每个学生信息有学号，姓名，三门课的成绩，输出三门课的总平均分以及所有成绩中最高的成绩及所对应的学生信息
void code2(){
    struct student{
        long num;
        char name[10];
        float score[3];
    } student[5]={
        {1001,"wang",67,88,99},
        {1002,"li",90,87,78},
        {1003,"zhao",88,77,66},
        {1004,"zhou",99,88,77},
        {1005,"chen",66,77,88}
    };

    int i,j,max,maxi;
    float aver[3]={0};
    for(j=0;j<3;j++){
        for (i=0;i<5;i++)
            aver[j]+=student[i].score[j];
        aver[j]/=5;
    }
    max=student[0].score[0];
    for(i=0;i<5;i++){
        for(j=0;j<3;j++){
            if(student[i].score[j]>max){
                max=student[i].score[j];
                maxi=i;
            }
        }
    }
    printf("平均成绩：\n");
    for(i=0;i<3;i++){
        printf("%6.1f",aver[i]);
        printf("\n");

    }
    printf("最高成绩：\n");
    printf("学号  姓名  成绩1  成绩2  成绩3\n");
    printf("%ld%8s",student[maxi].num,student[maxi].name);
    for(j=0;j<3;j++){
        printf("%8.1f",student[maxi].score[j]);
    }
    printf("\n");
}
//主要代码
int  main(){
    //code1();
    code2();
    return 0;
}