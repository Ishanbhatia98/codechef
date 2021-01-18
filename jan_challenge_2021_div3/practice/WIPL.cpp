//Solution provided by the Editorial
//Gives 100pts in c++ and 30pts in python3
//Same solution inn python3 Gives TLE for subtask2
#include<bits/stdc++.h>

#define ll long long
#define INF 1000000000

using namespace std;

int main(){
	ll t;
	cin >> t;
	while(t--){
		ll n, k;
		cin >> n >> k;
		ll v[n];
		for(int i=0;i<n;i++){
			int inp;
			cin >> inp;
			v[i] = inp;

		};
		
		sort(v, v+n);
		
		/*	
		cout << endl;
		cout << "Sorted array: ";
		for(auto e:v){
			cout << e << " ";
		};
		cout << endl;
		*/

		ll suf[n+1];
		suf[n] = 0;
		for(ll i = n-1;i>=0;i--){
			suf[i] = v[i]+suf[i+1];
		};
		
		/*
		cout << endl;
		cout << "Suffix array: ";
		for(ll i =0;i<=n;i++){
			cout << suf[i] << " ";
		};
		cout << endl;
		*/
		
		ll dp[n+1][k+1];
		for(ll i=0;i<=n;i++){
			for(ll j=0;j<=k;j++){
				dp[i][j] = INF;
			};
		};

		for(ll i=n-1;i>=0;i--){
			for(ll j=k;j>=0;j--){
				if(v[i]>=j){
					dp[i][j] = v[i];
					continue;
				}
				//else
				if(dp[i+1][j-v[i]]==INF){
						dp[i][j] = INF;
				}else{
						dp[i][j] = min(dp[i+1][j], v[i]+dp[i+1][j-v[i]]);
				}

					
				

			};
		};
		
		/*
		for(ll i=0;i<=n;i++){
			for(ll j =0;j<=k;j++){
				cout << dp[i][j] << " ";
			};
			cout << endl;
		};
		*/

		//cout << "ans: ";
		bool flag = true;
		for(ll i = n;i>=0;i--){
			if(suf[i]-dp[i][k]>=k){
				cout << n-i << endl;
				flag = false;
				break;
			}
		};
		if(flag){
			cout << -1 << endl;
		}
		

	};
	return 0;

}
