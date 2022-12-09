//Author:@syedrajo20
// task 3: Jack and Jill

#include<bits/stdc++.h>

#define nl "\n";
#define all(a) a.begin(), a.end()
#define fast ios_base::sync_with_stdio(0); cin.tie(0)
#define file freopen("task3_input.txt", "r", stdin);freopen("task3_output.txt", "w", stdout)

using namespace std;
typedef long long int ll;
const int N = 1e5+10;
const int INF = 1e9+10;

int main(){
	fast; // faster I/O
	#ifndef EPSILON
		file;
    #endif
    // code to solution...

	int n;
	cin >> n;
	vector<int> tasks(n);
	for (int i = 0; i < n; i++){
		cin >> tasks[i];
	}

	sort(tasks.begin(), tasks.end()); // sorting the array in ascending order of time

	stack<int> jack;
	vector<int> sequence;

	int jackTime = 0, jillTime = 0;

	string callString;
	cin >> callString;

	int i = 0;
	for (auto c : callString){
		if (c == 'J'){
			jack.push(tasks[i]);
			sequence.push_back(tasks[i]);
			jackTime += tasks[i];
			i++;

		}
		else{
			int val = jack.top();
			jack.pop();
			sequence.push_back(val);
			jillTime += val;		}
	}


	for (auto &val : sequence){
		cout << val;
	}
	cout << nl;
	cout << "Jack will work for "<< jackTime << " hours" << nl;
	cout << "Jill will work for "<< jillTime << " hours" << nl;
	return 0;
}
