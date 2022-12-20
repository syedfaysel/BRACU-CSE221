//Author:@syedrajo20
// BFS using queue

#include<bits/stdc++.h>

#define nl "\n";
#define all(a) a.begin(), a.end()
#define fast ios_base::sync_with_stdio(0); cin.tie(0)
#define file freopen("bfsInput.txt", "r", stdin);freopen("bfsOutput.txt", "w", stdout)

using namespace std;
typedef long long int ll;

vector<int> adj[100];
int visited[100];

// s = start vertex, n = number of vertices
void bfs(int s, int n){

	// make all node unvisited
	for (int i = 0; i <= n; i++) visited[i] = 0;

	queue<int> Q;
	Q.push(s);
	visited[s] = 1;


	while(!Q.empty()){

		int u = Q.front();
		Q.pop();
		cout << u << nl;

		for (int i = 0; i < adj[u].size(); i++){
			if (visited[adj[u][i]] == 0){
				int v = adj[u][i];
				visited[v] = 1;
				Q.push(v);
			}
		}
	}
}


int main(){
	fast; // faster I/O
	#ifndef EPSILON
		file;
    #endif
    // code...

	int n, m;
	cin >> n >> m;

	int u, v;
	for (int i = 0; i < m; i++){
		cin >> u >> v;
		// assuming undirected graph
		adj[u].push_back(v);
		adj[v].push_back(u);
	}

	bfs(1,n);

	return 0;
}
