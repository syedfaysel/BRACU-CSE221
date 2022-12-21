//Author:@syedrajo20
// Dijkstra algo (using set)

#include<bits/stdc++.h>

#define nl "\n";
#define all(a) a.begin(), a.end()
#define fast ios_base::sync_with_stdio(0); cin.tie(0)
#define file freopen("dijkstra1Input.txt", "r", stdin);freopen("dijkstraOutput.txt", "w", stdout)

using namespace std;
typedef long long int ll;
const int N = 1e5+10;
const int INF = 1e5;


int main(){
	fast; // faster I/O
	#ifndef EPSILON
		file;
    #endif
    // code...

	int n, m;
	cin >> n >> m;
	vector<int> dist(n+1, INF);

	vector<vector<pair<int, int>>> graph(n+1);
	int u, v, w;
	while(m--){
		cin >> u >> v >> w;
		// undirected graph
		graph[u].push_back({v, w});
		graph[v].push_back({u, w});
	}

	int source; cin >> source;
	dist[source] = 0;

	// s = {weight, vertex}
	set<pair<int, int>> s;
	s.insert({0, source});
	while(!s.empty()){
		auto x = *(s.begin()); // vertex with smalles weight
		s.erase(x);

		for (auto it : graph[x.second]){
			if (dist[it.first] > dist[x.second] + it.second){
				s.erase({dist[it.first], it.first});
				dist[it.first] = dist[x.second] + it.second;
				s.insert({dist[it.first], it.first});
			}
		}

	}

	for (int i = 1; i <= n; i++){
		if (dist[i] == INF){
			cout << -1 << " ,";
		}
		else cout << dist[i] << " ,";
	}
	return 0;
}
