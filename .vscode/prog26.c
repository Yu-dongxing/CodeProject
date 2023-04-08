#include<stdio.h>
int main(){
    int  a,c,u;
    int *b,*d,*e;
    b = &a;
    d = &c;
    e = &u;
    scanf("%d,%d",&a,&c);
    if (a<c){
        *e = *d;
        *d = *b;
        *b = *e;
    }
    printf("a:%d,b:%d",*b,*d);
    return 0;
}