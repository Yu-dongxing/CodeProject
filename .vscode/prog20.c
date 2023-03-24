#include <stdio.h>
#include <string.h>

#define MAX_STUDENTS 100

struct Student {
char name[50];
int id;
float gpa;
};

int main() {
struct Student students[MAX_STUDENTS];
int num_students = 0;

while (1) {
    printf("请输入英文 (添加[add], 列出[list], 取消[quit]): ");
    char command[10];
    scanf("%s", command);

    if (strcmp(command, "add") == 0) {
        if (num_students >= MAX_STUDENTS) {
            printf("Error: too many students\n");
            continue;
        }

        struct Student new_student;
        printf("输入学生姓名: ");
        scanf("%s", new_student.name);
        printf("输入学生号: ");
        scanf("%d", &new_student.id);
        printf("输入学生绩点: ");
        scanf("%f", &new_student.gpa);

        students[num_students] = new_student;
        num_students++;

        printf("学生姓名:%s\n学生号:%d\n学生绩点%.2f\n", new_student.name, new_student.id, new_student.gpa);
    } else if (strcmp(command, "list") == 0) {
        printf("Name\tID\tGPA\n");
        for (int i = 0; i < num_students; i++) {
            printf("%s\t%d\t%.2f\n", students[i].name, students[i].id, students[i].gpa);
        }
    } else if (strcmp(command, "quit") == 0) {
        break;
    } else {
        printf("Error: invalid command\n");
    }
}

return 0;
}
