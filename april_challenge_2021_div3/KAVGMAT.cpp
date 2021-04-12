
#include <bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
    ll tc;
    cin >> tc;
    while (tc--)
    {
        ll n, m, kk;
        cin >> n >> m >> kk;
        double matrix[n + 1][m + 1];
        for (ll i = 0; i <= n; i++)
        {
            for (ll j = 0; j <= m; j++)
            {
                if (i == 0 || j == 0)
                {
                    matrix[i][j] = 0;
                }
                else
                {
                    cin >> matrix[i][j];
                }
            }
        }
        for (ll i = 0; i <= n; i++)
        {
            double px = 0;
            for (ll j = 0; j <= m; j++)
            {
                matrix[i][j] += px;
                px = matrix[i][j];
            }
        }
        for (ll j = 0; j <= m; j++)
        {
            double px = 0;
            for (ll i = 0; i <= n; i++)
            {
                matrix[i][j] += px;
                px = matrix[i][j];
            }
        }
        ll mins = min(n, m);
        ll ans = 0;
        for (ll len = 1; len <= mins; len++)
        {
            for (ll i = len; i <= n; i++)
            {
                for (ll j = len; j <= m; j++)
                {
                    if ((matrix[i][j] + matrix[i - len][j - len] - matrix[i][j - len] - matrix[i - len][j]) / (len * len) >= kk)
                    {
                        ans++;
                    }
                }
            }
        }
        cout << ans << endl;
    }
}