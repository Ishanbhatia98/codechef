from math import ceil

def findmax(n, m):
    mx = max(n, m)
    mn = min(n, m)
    e = ceil(mx/2)
    en = ceil(mn/2)
    o = mx-e
    on = mn-en

    return e*en+o*on

def convert(s):
    l = []
    for i in s:
        if i=='.':
            l.append(0)
        else:
            l.append(1)
    return l
for _ in range(int(input())):
    n, m = map(int, input().split())
    matrix = [convert(input()) for _ in range(n)]
    t = findmax(n, m)
    #TODO: write subtask2

