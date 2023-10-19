//题解【洛谷】P1002 过河卒
/*棋盘上 A 点有一个过河卒，
需要走到目标 B 点。
卒行走的规则：可以向下、或者向右。
同时在棋盘上 C 点有一个对方的马，
该马所在的点和所有跳跃一步可达的点称为对方马的控制点。
因此称之为“马拦过河卒”。
思路
这是一道NOI普及组的原题，我用的是递推来做。
把马能到达的点设为已访问
先把第一行初始化，
    每个点的方案数=左边的方案数(并且不是马的控制点)
再把第一列初始化，
    每个点的方案数=上面的方案数(并且不是马的控制点)
之所以能这么做，是因为卒只能向右或下走
按照公式求出到每个点有多少种走法(f(i,j)=f(i-1,j)+f(i,j-1))
输出走到右下角的点的个数
*/
/*	代码出现问题*/
#include <iostream>
using namespace std;
typedef unsigned long long ull;
const int N=30;
int dx[8]={-2,-1,1,2,2,1,-1,-2};
int dy[8]={1,2,2,1,-1,-2,-2,-1};
int n,m,x,y;
bool st[N][N];
ull f[N][N];
int main()
{
	cin>>n>>m>>x>>y;
	st[x][y]=true;
	for(int i=0; i<8; i++)
	{
		int tx=x+dx[i],ty=y+dy[i];
		st[tx][ty]=true;
	}
	f[0][0]=1;
	for(int j=1; j<=m; j++)
		if(!st[0][j])
			f[0][j]=f[0][j-1];
	for(int i=1; i<=n; i++)
		if(!st[i][0])
			f[i][0]=f[i-1][0];
	for(int i=1; i<=n; i++)
		for(int j=1; j<=m; j++)
			if(!st[i][j])
				f[i][j]=f[i][j-1]+f[i-1][j];
	cout<<f[n][m]<< endl;
	return 0;
}
