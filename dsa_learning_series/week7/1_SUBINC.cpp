
/*Longest Increasing Subsequence and Kadanes algorithm are pre-requisites to solve this problem*/
#include<iostream>
#include<vector>


using namespace std;

int main(){
	int t;
	cin >> t;
	while(t--){
		int n;
		cin >> n;
		vector<long long> v;
		for(int i=0;i<n;i++){
			long long inp;
			cin >> inp;
			v.push_back(inp);
		};
		long long dp[n];
		for(int i=0;i<n;i++){
			dp[i] = 1;
		};
		for(int i=1;i<n;i++){
			if(v[i]>=v[i-1]){
				dp[i] = max(dp[i], 1+dp[i-1]);
			}
		};
		long long sum = 0;
		for(int i=0;i<n;i++){
			sum+=dp[i];
		};
		cout << sum << endl;
	};
	return 0;
}
