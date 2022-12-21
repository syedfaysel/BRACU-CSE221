# All about graph

## Graph Traversal
1. BFS (Breadth First Search)
2. DFS (Depth First Search)

### BFS

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> adj[100];
bool visited[100];

void bfs(int s){

	queue<int> Q;
	Q.push(s);
	visited[s] = true;


	while(!Q.empty()){

		int u = Q.front();
		Q.pop();
		cout << u << " ";

		for (auto &v : adj[u]){

			if (!visited[v]){
				visited[v] = true;
				Q.push(v);
			}
		}
	}
}


int main(){

	// n = vertices, m = edges
	int n, m;
	cin >> n >> m;
	// mark all vertices as unvisited
	for (int i = 0; i <= n; i++) visited[i] = false;

	// create adj list
	int u, v;
	while(m--){
		cin >> u >> v;
		// assuming undirected graph
		adj[u].push_back(v);
		adj[v].push_back(u);
	}

	// call bfs(start)
	bfs(1);
	return 0;
}
```

### DFS

```cpp
#include<bits/stdc++.h>
using namespace std;


vector<int> adj[100]; //adjacent list
bool visited[100];


void dfs(int node){
	visited[node] = true;
	cout << node << " ";

	for (auto &it : adj[node]){

		if (!visited[it]){
			dfs(it);
		}
	}
}

int main(){

	// n = vertices, m = edges
	int n, m;
	cin >> n >> m;
	// mark all vertices as unvisited
	for (int i = 0; i <= n; i++) visited[i] = false;

	// create adj list
	int u, v;
	while(m--){
		cin >> u >> v;
		// assuming undirected graph
		adj[u].push_back(v);
		adj[v].push_back(u);
	}


	// call dfs(start)
	dfs(1);
	return 0;
}
```

Note: instead of writing for (auto &it : adj[node])... we can write it in different ways:

```cpp
	for (int i = 0; i < adj[node].size(); i++){
		if (!visited[adj[node][i]]){
			dfs(adj[node][i]);
		}
	}
```
