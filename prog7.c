#include <stdio.h>
int main()
{
    int a = 21;
    int b = 10;
    int c ;

    c = a + b;
    printf("line 1 - c 的值是 %d\n", c);

    c = a - b ;
    printf("line 2 - c 的值是 %d\n",c);

    c = a * b;
    printf("line 3 - c 的值是 %d\n",c);

    c = a / b ;
    printf("line 4 - c 的值是 %d\n",c);
    c = a % b ;
    printf("line 5 - c 的值是 %d\n",c);
    c = a++;
    printf("line 6 - c 的值是 %d\n",c);
    c = a--;
    printf("line 7 - c 的值是 %d\n",c);
    

}