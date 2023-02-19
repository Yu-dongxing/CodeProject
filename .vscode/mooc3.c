#include <stdio.h>
#include <stdlib.h>

int main()

{
  float x,y,z,t;

  double  A;

  printf("请输入四次捐款额度；");

  scanf ("%f %f %f %f",&x,&y,&z,&t);

      if (x>0&&y>0&&z>0&&t>0&&z>t){

          A=(x+y+(z-t)+0.00);

          printf("%0.2f",A);
         }
      else {
          printf("error");
    }
    return 0;
}