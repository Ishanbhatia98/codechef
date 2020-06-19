#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

long long longestprefix(string s)
{
    long long status = 0;
    long long total = 0;
    for (long long i = 0; i < s.size(); ++i)
    {
        if (s[i] == '<')
        {
            status++;
        }
        else
        {
            status--;
        }
        if (status < 0)
        {
            return total;
        }
        if (status == 0)
        {
            total = max(total, i + 1);
        }
    }
    return total;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string s;
        cin >> s;
        cout << longestprefix(s) << endl;
    };

    return 0;
}