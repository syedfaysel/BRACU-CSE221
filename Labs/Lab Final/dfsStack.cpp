//Author:@syedrajo20
// DFS using stack

#include<bits/stdc++.h>

#define nl "\n";
#define all(a) a.begin(), a.end()
#define fast ios_base::sync_with_stdio(0); cin.tie(0)
#define file freopen("dfsInput.txt", "r", stdin);freopen("dfsOutput.txt", "w", stdout)

using namespace std;
typedef long long int ll;
const int N = 1e5+10;
const int INF = 1e9+10;

vector<int> adj[100];
bool visited[100];

void dfs(int node){
	// preorder traversal
	visited[node] = 1;
	cout << node << " ";

	//  inorder
	vector<int>::iterator it;
	for (it = adj[node].begin(); it != adj[node].end(); it++){

		if (visited[*it]);
		else{
			dfs(*it);
		}
	}

	// postorder traversal: to print post order
	// cout << node << " ";

}

int main(){
	fast; // faster I/O
	#ifndef EPSILON
		file;
    #endif
    // code...
	int n, m;
	cin >> n >> m;
	for (int i = 0; i <= n; i++) visited[i] = false;
	int u, v;
	while(m--){
		cin >> u >> v;
		adj[u].push_back(v);
		adj[v].push_back(u);
	}

	dfs(1);

	return 0;
}
