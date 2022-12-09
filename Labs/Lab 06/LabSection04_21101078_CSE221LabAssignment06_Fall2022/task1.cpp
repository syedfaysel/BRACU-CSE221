// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>

#define nl "\n";
#define all(a) a.begin(), a.end()
#define fast ios_base::sync_with_stdio(0); cin.tie(0)
#define file freopen("task1_input.txt", "r", stdin);freopen("task1_output.txt", "w", stdout)

using namespace std;
typedef long long int ll;
const int N = 1e5+10;
const int INF = 1e9+10;

int main() {
	
    fast; // faster I/O
    #ifndef EPSILON
        file;
    #endif

    // solution code starts here...

    int n; cin >> n;
    
    vector<pair<int, int>> task, selected;

    for (int i = 0; i < n; i++){
        int a, b; cin >> a >> b;
        task.push_back(make_pair(b, a));
    }

    sort(task.begin(), task.end());

    int  prev;
    for (int i = 0; i < n; i++){
        if (selected.size() == 0){
            selected.push_back(task[0]);

        }
        // set prev to the finish time of the previous selected task
        
        prev = selected.back().first;
        if(prev <= task[i].second ){
            selected.push_back(task[i]);
        }
    }

    // Print Selected Activity
    cout << selected.size() << "\n";
    for (auto &val : selected){
        cout << val.second << " " << val.first << "\n";
    }

    return 0;
}


