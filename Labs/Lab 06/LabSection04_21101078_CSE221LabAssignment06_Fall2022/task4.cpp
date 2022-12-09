//Author:@syedrajo20
// Task 4: Squre Number

#include<bits/stdc++.h>

#define nl "\n";
#define all(a) a.begin(), a.end()
#define fast ios_base::sync_with_stdio(0); cin.tie(0)
#define file freopen("input4.txt", "r", stdin);freopen("output4.txt", "w", stdout)

using namespace std;
typedef long long int ll;
const int N = 1e5+10;
const int INF = 1e9+10;

int main(){
	fast; // faster I/O
	#ifndef EPSILON
		file;
    #endif

    // solution code starts here...

	int a, b;
	while(true){
		cin >> a >> b;
		if (a == 0 and b == 0){
			break;
		}
		int ans = 0;
		for (int i = a; i * i <= b; i++){
			ans++;
		}
		cout << ans << nl;
	}

	return 0;
}
