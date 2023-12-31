#include<stdio.h>
int main(){
    int x,y,z,m;

    scanf("%d%d%d",&x,&y,&z);
    if(x>0&&y>0||z>=0){
        if(y>z*50){
            m=x+y-50*z;
        }
        else{
            m=x;
        }
        printf("%d",m);
    }else{
        printf("error");
    }
    return 0;
}