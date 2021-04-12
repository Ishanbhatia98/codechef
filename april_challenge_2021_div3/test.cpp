
#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
using cmpl = complex<long double>;
constexpr int MAXN = (int)1e6;
int dp[MAXN + 2], dp1[MAXN + 2];
int next0[MAXN], next1[MAXN];
void spar()
{
    string s;
    cin >> s;
    int n = s.length();
    int last_pos = -1;
    for (int i = 0; i < n; i++)
    {
        if (s[i] == '0')
        {
            for (int j = last_pos + 1; j <= i; ++j)
            {
                next0[j] = i;
                last_pos = i;
            }
        }
        for (int i = last_pos + 1; i < n; ++i)
            next0[i] = n;
        if (next0[0] == n)
        {
            cout << "0\n";
            return;
        }
        last_pos = -1;
        for (int i = 0; i < n; ++i)
        {
            if (s[i] == '1')
            {
                for (int j = last_pos + 1; j <= i; ++j)
                {
                    next1[j] = i;
                    last_pos = i;
                }
            }
            for (int i = last_pos + 1; i < n; ++i)
                next1[i] = n;

            dp[n] = dp[n + 1] = 0;
            dp1[n] = dp1[n + 1] = 0;
            for (int i = n - 1; i >= 0; --i)
            {
                dp[i] = dp[i + 1];
                if (s[i] == '0' && next1[i] < n)
                    dp[i] = max(dp[i], dp[next1[i] + 1] + 1);
                if (s[i] == '1' && next0[i] < n)
                    dp[i] = max(dp[i], dp[next0[i] + 1] + 1);
                dp1[i] = dp1[i + 1];
                if (next1[i] < n)
                    dp[i] = max(dp[i], dp[next1[i] + 1] + 1);
            }
            int len = dp1[0] + 1;
            int cu = next1[0] + 1;
            string ans = "1";
        }
    }
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        spar();
    }
    return 0;
}