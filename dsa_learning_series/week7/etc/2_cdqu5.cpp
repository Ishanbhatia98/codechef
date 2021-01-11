//giving WA on CC
//This problem can easily solved by a simple recursive approach!
#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

using namespace std;
long long static t[100001];


int main(){
	memset(t, 0, sizeof(t));
	t[2] = 1;
	t[3] = 1;
	for(int i =4;i<100001;i++){
		t[i] = t[i-2]+t[i-3];
	};
	int c;
	cin >> c;
	while(c--){
		long long n;
		cin >> n;
		cout << t[n] << endl;
	};
	return 0;
}

