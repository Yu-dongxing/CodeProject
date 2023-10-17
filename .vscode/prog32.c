//使用穷举法
//口袋中有红，橙，黄，绿，蓝颜色的球各一些，现在从口袋中每次摸出三个求，要求颜色均不同，考虑摸出的顺序，输出所有可能的取法及数量
#include<stdio.h>

void code1(){
    enum color{red,orange,yellow,green,blue}c,x,y,z;
    int i,n=0;
    for(x=red;x<=blue;x++){
        for(y=red;y<=blue;y++) if(x!=y){
        for(z=red;z<=blue;z++){
            if(z!=x && z!=y){
                n++;
                printf("%-3d",n);
                for(i=1;i<=3;i++){
                    switch(i){
                        case 1:c=x;break;
                        case 2:c=y;break;
                        case 3:c=z;

                    }
                    switch (c){
                        case red:printf("%-8s","red");break;
                        case orange:printf("%-8s","orange");break;
                        case yellow:printf("%-8s","yellow");break;
                        case green:printf("%-8s","green");break;
                        case blue:printf("%-8s","blue");
                    }
                }printf("\n");

            }printf("n=%d\n",n);
        }
        }
    }
}
/*
#include <stdio.h>  
enum color { red, orange, yellow, green, blue };  
void code1() {  
    enum color x, y, z;  
    int i, n = 0;  
    for (x = red; x <= blue; x++) {  
        for (y = red; y <= blue; y++) {  
            if (x != y) {  
                for (z = red; z <= blue; z++) {  
                    if (z != x && z != y) {  
                        n++;  
                        printf("%-3d", n);  
                        for (i = 1; i <= 3; i++) {  
                            switch (i) {  
                                case 1:  
                                    printf("%-8s", color_names[x]);  
                                    break;  
                                case 2:  
                                    printf("%-8s", color_names[y]);  
                                    break;  
                                case 3:  
                                    printf("%-8s", color_names[z]);  
                                    break;  
                            }  
                        }  
                        printf("\n");  
                    }  
                }  
            }  
        }  
    }  
    printf("n=%d\n", n);  
}  
  
int main() {  
    const char *color_names[] = { "red", "orange", "yellow", "green", "blue" };  
    code1();  
    return 0;  
}
*/
//----------------------------------------------------------------------------------------
int main(){
    code1();
    return 0;
}