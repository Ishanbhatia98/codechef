#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t;
    cin >> t;
    while (t--)
    {
        ll n;
        cin >> n;
        string s;
        cin >> s;
        ll a = 0, b = 0;
        for (ll i = 0; i < n; i++)
        {
            if (s[i] == '1')
            {
                b++;
            }
            else
            {
                a++;
            }
        }
        vector<ll> factors;
        for (ll i = 1; i <= sqrt(n); i++)
        {
            if (n % i == 0)
            {
                if (n / i == i)
                {
                    factors.push_back(i);
                }
                else
                {
                    factors.push_back(n / i);
                    factors.push_back(i);
                }
            }
        }
        ll ans = 1e9;
        for (auto fact : factors)
        {
            vector<ll> freq(fact);
            for (ll i = 0; i < fact; i++)
            {
                for (ll j = i; j < n; j += fact)
                {
                    if (s[j] == '1')
                    {
                        freq[i]++;
                    }
                }
            }
            ll req = n / fact;
            for (ll i = 0; i < fact; i++)
            {
                ll x = req - freq[i];
                x += (b - freq[i]);
                ans = min(ans, x);
            }
        }
        cout << ans << endl;
    }
}