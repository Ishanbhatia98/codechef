#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long count(vector<long long> v)
{
    long long m = 1000000000;
    long long total = 0;
    for (auto i : v)
    {
        m = min(m, i);
        total += m;
    }
    return total;
}
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<long long> v;
        for (int i = 0; i < n; i++)
        {
            long long z;
            cin >> z;
            v.push_back(z);
        }

        cout << count(v) << endl;
    }

    return 0;
}