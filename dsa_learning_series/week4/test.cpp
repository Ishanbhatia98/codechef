#include <bits/stdc++.h>

#define pb push_back
#define ll long long
using namespace std;
ll f(vector<ll> v, int l, int r)
{
    if (l > r)
        return 0;
    int m = l + (r - l) / 2;
    ll t = 0;
    for (int i = l; i <= m; i++)
    {
        for (int j = m; j <= r; j++)
        {
            if (i != j)
                t += (v[i] > v[j]);
        };
    };
    return t + f(v, l, m - 1) + f(v, m + 1, r);
}
int main()
{
    int n;
    cin >> n;
    vector<ll> v;
    for (int i = 0; i < n; i++)
    {
        ll inp;
        cin >> inp;
        v.pb(inp);
    };
    cout << f(v, 0, n - 1) << endl;

    return 0;
}