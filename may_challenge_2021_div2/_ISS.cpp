#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int n = 4e6 + 5;
    int phi[n], ans[n];
    for (int i = 0; i < n; i++)
    {
        phi[i] = i;
        ans[i] = 0;
    }
    for (int p = 2; p < n; p++)
    {
        if (phi[p] == p)
        {
            phi[p] = p - 1;
            for (int i = 2 * p; i < n; i += p)
                phi[i] = (phi[i] / p) * (p - 1);
        }
    }
    for (int i = 1; i < n; i++)
    {
        ans[i] += i - 1;
        for (int j = 2 * i; j < n; j += i)
        {
            ans[j] += i * ((1 + phi[j / i]) / 2);
        }
    }
    int x;
    cin >> x;
    while (x--)
    {
        int K;
        cin >> K;
        cout << ans[4 * K + 1] << "\n";
    }
    return 0;
}