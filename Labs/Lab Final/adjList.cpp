//Author:@syedrajo20
// Adjlist

#include<bits/stdc++.h>

#define nl "\n";
#define all(a) a.begin(), a.end()
#define fast ios_base::sync_with_stdio(0); cin.tie(0)
#define file freopen("adjList_input.txt", "r", stdin);freopen("adjList_output.txt", "w", stdout)

using namespace std;
typedef long long int ll;


int main(){
	fast; // faster I/O
	#ifndef EPSILON
		file;
    #endif
    // code...

	int n, m;
	cin >> n >> m;
	vector<int> adjList[n+1];
	int u, v, w;
	while(m--){
		cin >> u >> v >> w;
		adjList[u].push_back(v);
	}

	for (int i = 1; i <= n; i++){
		cout << i << ": ";
		for (auto vertex : adjList[i]){
			cout << vertex << ", ";
		}
		cout << nl;
	}

	return 0;
}
