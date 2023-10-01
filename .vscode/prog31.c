//结构体 输入3个学生的信息后输出，信息包括学号，姓名，和4个课程的成绩
#include <stdio.h>
int main(){
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