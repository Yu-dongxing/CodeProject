/*选择法排序*/
#include <stdio.h>
int main(){
    int i,j;
    int a[10];
    int itemp;
    int ipos;
    printf("请输入10个整数：\n");               /*输入10个数，为数组元素赋值*/
    for(i=0;i<10;i++){
        scanf("%d",&a[i]);
    }
    
    /*使用选择法对数组元素从小到大排序*/
    
    for(i=0;i<9;i++){                         /*设置外层循环下标为0-8，表示前9个数组元素*/
        itemp=a[i];                           /*假设当前元素为最小值*/
        ipos=i;                               /*记录最小元素位置*/
        for(j=i+1;j<10;j++){                  /*设置内层循环下标为i+1~9,表示剩下的未排序数组元素部分*/                
            if(a[j]<itemp){                   /*如果当前元素比最小元素小，则将当前元素赋值给最小元素，并记录最小元素位置*/
                itemp=a[j];                   /*重新设置最小值*/
                ipos=j;                         /*修正最小元素位置*/
            }
        }
        a[ipos]=a[i];                           /*此两行代码用于将最小的数组元素和当前排序次数对应的数组元素互换*/
        a[i]=itemp;
    }
    printf("排序后的数组：\n");                     /*输出数组*/
    for(i=0;i<10;i++){
        printf("%d\t",a[i]);                        /*用制表位分隔数据*/
        if(i==4)                                    /*如果是第五个元素*/
            printf("\n");                              /*输出换行*/
    }
    printf("\n");
    return 0;                                       /*结束*/
}