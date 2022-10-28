#include<bits/stdc++.h>
using namespace std;


const int N = 1e5+5;
vector<int> adj_list[N];
bool visited[N];
void dfs(int current){
    visited[current] = true;
    for (int next_vertex : adj_list[current]){
        if (visited[next_vertex]) continue;
        dfs(next_vertex);
    }

}

int main(){

}

// Time complexity is O(V+E) also the space complexity
