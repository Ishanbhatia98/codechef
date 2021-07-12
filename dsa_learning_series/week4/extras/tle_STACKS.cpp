#include <bits/stdc++.h>
#define pb push_back
#define ll long long
using namespace std;
ll bs(vector<ll> v, ll l, ll r, ll x)
{
    if (l > r)
        return l;
    ll m = l + (r - l) / 2;

    if (v[m] > x)
        return bs(v, 0, m - 1, x);
    return bs(v, m + 1, r, x);
}

int main()
{
    ll t;
    cin >> t;
    while (t--)
    {
        ll n;
        cin >> n;
        vector<ll> a;
        for (ll i = 0; i < n; i++)
        {
            ll inp;
            cin >> inp;
            a.pb(inp);
        };

        vector<ll> v;
        v.pb(a[0]);
        ll m = a[0];
        for (ll i = 1; i < n; i++)
        {
            m = v[v.size() - 1];
            if (a[i] >= m)
            {
                v.pb(a[i]);
            }
            else
            {
                ll r = bs(v, 0, v.size() - 1, a[i]);

                v[r] = a[i];
            }
        };
        cout << v.size() << " ";
        for (ll i = 0; i < v.size(); i++)
        {
            cout << v[i] << " ";
        };
    };

    return 0;
}