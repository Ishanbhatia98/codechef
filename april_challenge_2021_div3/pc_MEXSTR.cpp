
#include <bits/stdc++.h>
#define ll long long int
using namespace std;
bool isSubse(string st1, string st2)
{
    int j = 0;
    for (int i = 0; i < st2.size(); i++)
    {
        if (st1[j] == st2[i])
            j++;
        if (j == st1.size())
            return true;
    }
    return false;
}
string generate_binary(string str)
{
    queue<string> queue;
    queue.push("1");
    while (true)
    {
        string s1 = queue.front();
        queue.pop();
        if (isSubse(s1, str) == false)
            return s1;
        string s2 = s1;
        queue.push(s1.append("0"));
        queue.push(s2.append("1"));
    }
}
int main()
{
    ll t;
    cin >> t;
    while (t--)
    {
        string s;
        cin >> s;
        int f = 0;
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] == '0')
            {
                f = 1;
                break;
            }
        }
        if (f == 0)
            cout << "0" << endl;
        else
            cout << generate_binary(s) << endl;
    }
}