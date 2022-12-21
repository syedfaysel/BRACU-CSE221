//Author:@syedrajo20
// Dijkstra (using priority queue)
// Source: Luv

#include<bits/stdc++.h>

#define nl "\n";
#define all(a) a.begin(), a.end()
#define fast ios_base::sync_with_stdio(0); cin.tie(0)
#define file freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout)

using namespace std;
typedef long long int ll;
const int N = 1e5+10;
const int INF = 1e9+10;



vector<pair<int, int>> graph[N];
vector<int> dist(N, INF);
vector<bool> visited(N, 0); // marked all vertices unvisited


void dijkstra(int source){


	set<pair<int, int>> s; //{weight, vertices}
	s.insert({0, source});
	dist[source] = 0;


	// like as bfs
	while(!s.empty()){

		auto node = *(s.begin()); //pair from set
		int v = node.second;
		int v_wt = node.first;
		s.erase(s.begin());
		if (visited[v]) continue;
		visited[v] = 1;


		for (auto child : graph[v]){
			int child_v = child.first;
			int child_wt = child.second;

			// if (new distance < current distance)
			if (dist[v] + child_wt < dist[child_v]){
				dist[child_v] = dist[v] + child_wt;
				s.insert({dist[child_v], child_v});
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
	int u, v, w;
	while(m--){
		cin >> u >> v >> w;
		// undirected & weighted graph
		graph[u].push_back({v, w});
		graph[v].push_back({u, w});
	}



	return 0;
}
