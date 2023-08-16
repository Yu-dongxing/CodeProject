/*冒泡法排序*/
#include <stdio.h>
int main(){
    int i,j;
    int a[10];
    int itemp;
    printf("请输入10个整数：\n");                   /*输入10个数*/
    for(i=0;i<10;i++){
        printf("a[%d]=",i);
        scanf("%d",&a[i]);
    }
    /*采用冒泡法使数组元素从小到大排序*/
    for(i=1;i<10;i++){
        
        for(j=9;j>=i;j--){

            if(a[j]<a[j-1]){
                //交换a[j]和a[j+1]
                itemp=a[j-1];

                a[j-1]=a[j];

                a[j]=itemp;

            }
        }
    }
    printf("排序后的数组：\n");

    for(i=0;i<10;i++){

        printf("%d\t",a[i]);

        if (i == 4)
        {
            printf("\n");
        }
        
}
    printf("\n");
    return 0;
}
