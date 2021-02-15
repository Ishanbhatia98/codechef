/*
 * Since checking for x!(factorial) is impossible due to it being a very very big number
 * we check for x, if there are more prime numbers than y before and including x then divyam wins the game
 * else chef wins it!
 * This code having the same logic gives TLE when coded in python!
 */
#include <bits/stdc++.h>
#define N 1000001
using namespace std;

int main()
{
	bool primes[N];
	memset(primes, true, sizeof(primes));

	int counts[N];

	for (int i = 2; ((i * i) < N); i++)
	{
		if (primes[i])
		{
			for (int j = i * i; j < N; j += i)
			{
				primes[j] = false;
			};
		}
	};

	int c = 0;
	for (int i = 2; i < N; i++)
	{
		if (primes[i])
		{
			c += 1;
		}
		counts[i] = c;
	};

	int t;
	scanf("%d", &t);
	while (t--)
	{
		int x, y;
		scanf("%d %d", &x, &y);
		if (counts[x] > y)
			printf("Divyam\n");
		else
			printf("Chef\n");
	};
	return 0;
}
