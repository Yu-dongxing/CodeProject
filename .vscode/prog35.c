/*
# [NOIP2000 提高组] 方格取数
## 题目描述
设有 $N \times N$ 的方格图 $(N \le 9)$，我们将其中的某些方格中填入正整数，而其他的方格中则放入数字 $0$。如下图所示（见样例）:
![](https://cdn.luogu.com.cn/upload/image_hosting/zj4bo91w.png)
某人从图的左上角的 $A$ 点出发，可以向下行走，也可以向右走，直到到达右下角的 $B$ 点。在走过的路上，他可以取走方格中的数（取走后的方格中将变为数字 $0$）。  
此人从 $A$ 点到 $B$ 点共走两次，试找出 $2$ 条这样的路径，使得取得的数之和为最大。
## 输入格式
输入的第一行为一个整数 $N$（表示 $N \times N$ 的方格图），接下来的每行有三个整数，前两个表示位置，第三个数为该位置上所放的数。一行单独的 $0$ 表示输入结束。
## 输出格式
只需输出一个整数，表示 $2$ 条路径上取得的最大的和。
## 样例 #1
### 样例输入 #1
```
8
2 3 13
2 6  6
3 5  7
4 4 14
5 2 21
5 6  4
6 3 15
7 2 14
0 0  0
```
### 样例输出 #1
```
67
```
## 提示
NOIP 2000 提高组第四题
*/
#include<bits/stdc++.h>
using namespace std;
int s[15][15],f[11][11][11][11],n=0;
int xin_dong_fang(int x,int y,int x2,int y2){
    if(f[x][y][x2][y2]!=-1){
        return f[x][y][x2][y2];

    }
    if(x==n&&y==n&&x2==n&&y2==n){
        return 0;

    }
    int m=0;
if (x<n&&x2<n){
		m=max(m,xin_dong_fang(x+1,y,x2+1,y2)+s[x+1][y]+s[x2+1][y2]-s[x+1][y]*(x+1==x2+1&&y==y2));
	}
    if (x<n&&y2<n){
		m=max(m,xin_dong_fang(x+1,y,x2,y2+1)+s[x+1][y]+s[x2][y2+1]-s[x+1][y]*(x+1==x2&&y==y2+1));
	}    
	if (y<n&&x2<n){
		m=max(m,xin_dong_fang(x,y+1,x2+1,y2)+s[x][y+1]+s[x2+1][y2]-s[x][y+1]*(x==x2+1&&y+1==y2));
	}
    if (y<n&&y2<n){
		m=max(m,xin_dong_fang(x,y+1,x2,y2+1)+s[x][y+1]+s[x2][y2+1]-s[x][y+1]*(x==x2&&y+1==y2+1));
	}
    f[x][y][x2][y2]=m;
    return m;
    
}

int main()
{
    cin>>n;
    for(int a=0;a<=n;a++){
    	for(int b=0;b<=n;b++){
      		for(int c=0;c<=n;c++){
      	 		for(int d=0;d<=n;d++){
					f[a][b][c][d]=-1;
				}
			}
		}
	}
    while(1){
   		int t=0,tt=0,ttt=0;
        cin>>t>>tt>>ttt;
        if(t==0&&tt==0&&ttt==0){
			break;
		}
        s[t][tt]=ttt;
	}
    cout<<xin_dong_fang(1,1,1,1)+s[1][1];
    return 0;
}