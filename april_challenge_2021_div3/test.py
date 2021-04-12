'''
using cmpl=complex<long double>;
constexpr int MAXN =(int)1e6;
int dp[MAXN + 2], dp1[MAXN + 2];
int next0[MAXN],next1[MAXN];
'''
M = 10**6
dp = [0 for _ in range(M)]
dp1 = [0 for _ in range(M)]
nx0 = [0 for _ in range(M)]
nx1 = [0 for _ in range(M)]
f = 0
for _ in range(int(input())):
    s = input()
    n = len(s)
    lp = -1
    for i in range(n):
        if s[i] == '0':
            for j in range(lp+1, i+1):
                nx[0][j] = i
                lp = i
        for i in range(lp+1, n):
            nx[0][i] = n
            if nx[0] == n:
                print(0)
                f = 1
                break
        if f:
            break
        lp -= 1
        for i in range(n):
            if s[i] == '1':
                for j in range(lp+1, i+1):
                    nx1 = i
                    lp = i

        last_pos = -1;
        for(int i=0; i < n; ++i){

            for(int i=last_pos + 1; i < n; ++i)
            next1[i] = n;

            dp[n] = dp[n+1] = 0;
            dp1[n] = dp1[n+1] = 0;
            for(int i=n-1; i >= 0; --1){
                dp[i] = dp[i+1];
                if(s[i] == '0' & & next1[i] < n)
                dp[i] = max(dp[i], dp[next1[i]+1]+1);
                if(s[i] == '1' & & next0[i] < n)
                dp[i] = max(dp[i], dp[next0[i]+1]+1);
                dp1[i] = dp1[i+1];
                if(next1[i] < n)
                dp[i] = max(dp[i], dp[next1[i]+1]+1);}
            int len = dp1[0]+1;
            int cu = next1[0]+1;
            string ans = "1";}
    }
}


int main() {
 // your code goes here
 return 0; }
