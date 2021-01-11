#include<iostream>
#include<cmath>
#include<algorithm>

using namespace std;

int main(){
	int t;
	cin >> t;
	while(t--){
		int n;
		cin >> n;
		int m = 0;
		while(n--){
			int s, p, v;
			
			cin >> s >> p >> v;
			int f = floor((float)(p/(s+1)));
			m = max(m, f*v);
		}
		cout << m << endl;
	
	}

	return 0;
}
