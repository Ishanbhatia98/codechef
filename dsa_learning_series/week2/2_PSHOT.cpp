#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<int> convert(string s)
{
    vector<int> v;
    for (auto i : s)
    {
        if (i == '1')
        {
            v.push_back(1);
        }
        else
        {
            v.push_back(0);
        }
    }
    return v;
}

int check(vector<int> v)
{
    //write code here
    int a, b;
    int rem;
    int n = v.size() / 2;
    a = b = 0;
    for (int i = 0; i < v.size(); ++i)
    {
        if ((i % 2) && (v[i] == 0))
        {
            b++;
        }
        if ((i % 2 == 0) && (v[i] == 0))
        {
            a++;
        }
        rem = ((2 * n - i - 1) / 2);

        if (a + rem < b)
        {
            return i + 1;
        }
        if (i % 2 == 0)
        {
            rem++;
        }

        if (b + rem < a)
        {
            return i + 1;
        }
    }
    return v.size();
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        string s;
        cin >> s;
        vector<int> v;
        v = convert(s);
        int i;
        i = check(v);
        cout << i << endl;
    };
    return 0;
}