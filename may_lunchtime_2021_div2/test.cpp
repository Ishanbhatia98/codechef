#include <bits/stdc++.h>

using namespace std;
const int MAX = 10000000;

int prefix[MAX + 1];

void buildPrefix()
{
    bool prime[MAX + 1];
    memset(prime, true, sizeof(prime));

    for (int p = 2; p * p <= MAX; p++)
    {

        if (prime[p] == true)
        {

            for (int i = p * 2; i <= MAX; i += p)
                prime[i] = false;
        }
    }

    prefix[0] = prefix[1] = 0;
    for (int p = 2; p <= MAX; p++)
    {
        prefix[p] = prefix[p - 1];
        if (prime[p])
            prefix[p]++;
    }
}
int query(int L, int R)
{
    return prefix[R] - prefix[L];
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int x;
    cin >> x;
    buildPrefix();
    while (x--)
    {
        int r;
        cin >> r;
        if (r == 2)
            cout << "1\n";
        else if (r == 3 || r == 4)
            cout << "2\n";
        else
        {
            int l = r / 2;
            int ans = query(l, r);
            cout << ans + 1 << "\n";
        }
    }
    return 0;
}