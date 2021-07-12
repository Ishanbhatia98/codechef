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

        multiset<ll> v;
        v.insert(a[0]);
        ll m = a[0];
        for (auto i = 1; i < n; i++)
        {
            auto r = v.upper_bound(a[i]);
            if (r != v.end())
            {
                v.erase(r);
                v.insert(a[i]);
            }
            else
            {
                v.insert(a[i]);
            }
                };
        cout << v.size() << " ";
        for (auto i = v.begin(); i != v.end(); i++)
        {
            cout << *i << " ";
        };
    };

    return 0;
}