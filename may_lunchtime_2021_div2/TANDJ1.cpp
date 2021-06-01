#include <iostream>
#include <cstdlib>
#define int long long
using namespace std;

void solve()
{
    int a, b, c, d, k;
    cin >> a >> b >> c >> d >> k;
    int x = abs(a - c);
    int y = abs(b - d);
    int total = k - (x + y);
    if (total < 0)
        cout << "NO"
             << "\n";
    else if (total % 2 == 0)
        cout << "YES"
             << "\n";
    else
        cout << "NO"
             << "\n";
}

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int x;
    cin >> x;
    while (x--)
    {
        solve();
    }
    return 0;
}