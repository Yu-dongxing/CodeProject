#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main() {
    srand((unsigned)time(NULL));
    int i =0;
    int random =0;
    for (; i < 5; i++) {
        random = rand();
        printf("%d", random);
    }
}