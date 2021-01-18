//Author solution

#include <bits/stdc++.h>

using namespace std;

const int N = 1e6 + 1;

int t, n, m;
long long ans;
vector <int> ant[N];
map <int, int> coord;
int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0);
    cin >> t;
    while (t--)
    {
        cin >> n;
        ans = 0;
        vector <int> distances;
        for (int i = 0; i < n; i++)
        {
            cin >> m;
            while (m--)
            {
                int x;
                cin >> x;
                coord[abs(x)]++;
                if (coord[abs(x)] == 1) distances.push_back(abs(x));
                ant[i].push_back(x);
            }
        }
        for (int i = 0; i < n; i++)
        {
            long long pos, neg;
            pos = neg = 0;
            vector<pair<int, int> > s;
            for (auto p : ant[i])
            {
                if (p < 0) neg++, s.push_back({abs(p), -1});
                else pos++, s.push_back({abs(p), 1});
            }
            sort(s.begin(), s.end());
            for (auto p : s)
            {
                if (p.second == -1) neg--;
                else pos--;
                if (coord[p.first] > 1)
                {
                    if (p.second == -1) ans += neg;
                    else ans += pos;
                }
                else
                {
                    if (p.second == 1) ans += neg;
                    else ans += pos;
                }
            }
        }
        for (auto p : distances) if (coord[p] > 1) ans++;
        cout << ans << endl;
        for (int i = 0; i < n; i++) ant[i].clear();
        coord.clear();
    }
    return 0;

}
