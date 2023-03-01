#include<cstdio>
#include<algorithm>
using namespace std ;
struct Node{
    int a,b,lx,ly;
}node[100010];
int main(){
    int n,x,y,ans,f=0;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        scanf("%d%d%d%d",&node[i].a,&node[i].b,&node[i].lx,&node[i].ly);
    scanf("%d%d",&x,&y);
    for(int i=n;i;i--)
        if(x >=node[i].a&&x<=node[i].a+node[i].lx&&y>=node[i].b&&y<=node[i].b+node[i].ly)
    return printf ("%d",i ),0;
    puts("-1");
    return 0;
}