from collections import Counter

n, k = map(int, input().split())

#K cannot be more than 1007, since there are only 1007 prime numbers between 0 and 8000(from constraints)
k = min(k, 1007)

l = list(map(int, input().split()))

#cnt maintains the frequency of all elements present in the list l
cnt = Counter(l)

#set(l) stores all elements of l without their duplicates
l = list(set(l))

#n now stores the value of the number of unique elements in the input list l
n = len(l)

mod = 10**9 + 7


dp = [[0 for _ in range(k+1)] for _ in range(n)]

#dp[0][0] is 1 since an empty subsequence is valid
dp[0][0] = 1

#dp[0][1] is the number of subsequence that can be formed by using 0th index element of l
dp[0][1] = cnt[l[0]]

for i in range(1, n):
    '''
    dp[i][0] is 1 since there is only one subsequence(empty set) that can be formed by using elemnts till the ith index 
    of l, when we can choose 0 elements.
    '''
    dp[i][0] = 1
    for j in range(1, k+1):
        '''
        dp[i][j]->
        The number of subsequences that can be formed using the first i elements of l, when we can choose j such elements.
        so for every element at an arbitary index i, there are two options.
        1)Do not choose i for the subsequence, thus j(k) does not reduce -> dp[i-1][j]
        2)Choose i, since i is not unique in the original input, we multiply this choice with its frequency to account
          for all its duplicates, also j(k) reduces by 1 since we chose the ith element -> dp[i-1][j-1]*cnt[l[i]]
        '''
        dp[i][j] = dp[i-1][j] +cnt[l[i]]*dp[i-1][j-1]
        dp[i][j]%=mod

'''
Since we can use Atmost K elements, we can use lesser elements as well
So the final answer is a sum of dp[n-1][0]+dp[n-1][1]...dp[n-1][k]
i.e sum of subsequences using first n-1 elements and choosing 0 elemnts+sum of subsequences using first n-1 elemnts and choosing 1 element+...sum of subsequence using first n-1 elements and choosing k elements.
n-1 -> all unique elements present in the original input list l.
'''
print(sum(dp[n-1][j] for j in range(k+1))%mod)
