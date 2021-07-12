#include <bits/stdc++.h>
#include <math.h>
#define ll long long

using namespace std;

ll m = pow(10, 9) + 7;

ll conv(ll a)
{
    if (a < 10)
        return a;
    ll b = a;
    a /= 10;
    ll t = 0;
    ll c = 1;
    while (a % 10 != a)
    {
        t *= 10;
        t += (a % 10);
        a /= 10;
        c++;
    };
    t *= 10;
    t += a;
    b = b * pow(10, c);
    return (b + t) % m;
}

ll power(ll x, ll y, ll p)
{
    ll res = 1;
    x %= p;
    if (x == 0)
        return 0;
    while (y > 0)
    {
        if ((y & 1) == 1)
        {
            res = (res * x) % p;
        }
        y >>= 1;
        x = (x * x) % p;
    }
    return res;
}
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        ll l, r;
        cin >> l >> r;
        ll total = 0;

        for (ll i = l + 1; i < r + 1; i++)
        {
            //cout << i << endl;
            //cout << conv(i) << endl;
            total += conv(i);
        };

        cout << power(conv(l), total, m) << endl;
        ;
    }
    return 0;
}