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
    printf("Enter command (add, list, quit): ");
    char command[10];
    scanf("%s", command);

    if (strcmp(command, "add") == 0) {
        if (num_students >= MAX_STUDENTS) {
            printf("Error: too many students\n");
            continue;
        }

        struct Student new_student;
        printf("Enter name: ");
        scanf("%s", new_student.name);
        printf("Enter ID: ");
        scanf("%d", &new_student.id);
        printf("Enter GPA: ");
        scanf("%f", &new_student.gpa);

        students[num_students] = new_student;
        num_students++;

        printf("Added student %s with ID %d and GPA %.2f\n", new_student.name, new_student.id, new_student.gpa);
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
