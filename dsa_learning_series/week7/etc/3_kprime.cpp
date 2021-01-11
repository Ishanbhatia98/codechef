//code not working as expected to
#include<iostream>
#define ll long long int
using namespace std;


ll static dp[100001][6];
ll static primes[100001];
int main(){
	memset(primes, 0, 100001);
	memset(dp, 0, sizeof(dp));
	/*
	 * working!
	for(auto i:primes){
                cout << i<< " ";
        };
	*/

	for(ll i=0;i<100001;i++){
		if(primes[i]==0){
			for(ll j=i;j<100001;j+=i){
				primes[j]+=1;
			};
		}
	};
	
	for(auto i:primes){
                cout << i<< " ";
        };

	for(ll i=0;i<100001;i++){
		if(primes[i]==0){
			primes[i]=1;
		}
	};
	/*
	for(auto i:primes){
		cout << i<< " ";
	};*/

	for(ll i=0;i<100001;i++){
		for(ll j=0;j<6;j++){
			dp[i][j] = dp[i-1][j]+(primes[i]==j);
		};
	};

	int t;
	cin >> t;
	while(t--){
		ll a, b, k;
		cin >> a >> b >> k;
		cout << dp[b][k]-dp[a-1][k]<<endl;
	};
	return 0;

}
