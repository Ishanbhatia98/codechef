#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
	int n;
	cin >> n;
	vector<int> s;
	for(int i=0;i<n;i++){
		int inp;
		cin >> inp;
		s.push_back(inp);
	};

	int stack = 0;
	int nesting_p = 1;
	int nesting_l = 0;
	

	int max_l = 0;
	int len_p = 1;
	int previous = 0;

	for(int i=0;i<n;i++){
		if (s[i]==1){
			stack++;
		}else{	
			if(stack>nesting_l){
				nesting_l = stack;
				nesting_p = i;
			}
			stack--;
		}
		if(stack==0){
			int l = i-previous+1;
			if(l>max_l){
				max_l = l;
				len_p = previous;
			}
			previous = i+1;
		}
	};

	cout << nesting_l << " " << nesting_p <<  " " << max_l << " " << len_p+1 << endl;
	return 0;
}
