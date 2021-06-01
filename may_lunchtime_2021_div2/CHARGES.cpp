#include <bits/stdc++.h>
#define cin(arr, n)             \
    for (int i = 0; i < n; i++) \
    cin >> arr[i]
typedef long long ll;
using namespace std;
int main()
{
    int xx;
    cin >> xx;
    while (xx--)
    {
        int n, k;
        cin >> n >> k;
        string s;
        cin >> s;
        int arr[k];
        cin(arr, k);

        if (n == 1)
        {
            for (int i = 0; i < k; i++)
                cout << 0 << endl;
            continue;
        }

        ll distance = 0;
        for (int i = 1; i < n; i++)
        {
            if (s[i] == s[i - 1])
                distance += 2;
            else
                distance += 1;
        }

        for (int i = 0; i < k; i++)
        {
            if (arr[i] == 1)
            {
                if (s[0] == s[1])
                    distance--;
                else
                    distance++;
            }
            else if (arr[i] == n)
            {
                if (s[n - 1] == s[n - 2])
                    distance--;
                else
                    distance++;
            }
            else
            {
                int temp = 0;
                if (s[arr[i] - 1] == s[arr[i] - 2])
                    temp = temp + 2;
                if (s[arr[i] - 1] != s[arr[i] - 2])
                    temp += 1;
                if (s[arr[i] - 1] != s[arr[i]])
                    temp += 1;
                if (s[arr[i] - 1] == s[arr[i]])
                {
                    temp++;
                    temp++;
                }

                if (temp == 4)
                    distance = distance - 2;
                if (temp == 2)
                    distance = distance + 2;
            }

            if (s[arr[i] - 1] == '0')
                s[arr[i] - 1] = '1';
            else
                s[arr[i] - 1] = '0';
            cout << distance << endl;
        }
    }
    return 0;
}