from collections import defaultdict as dd
for _ in range(int(input())):
    n = int(input())
    s = list(input().split())
    d = dd(lambda:set())
    
    #Taking the body(w[1:]) of the words(w) in list of words(s) as keys.
    for w in s:
        d[w[1:]].add(w[0])
    #bs -> list of keys i.e list of unique values of bodies(w[1:]) of words.
    bs = list(d.keys())
    '''
    According to the rules;
    Chosen words should not be funny, but swapping the first letters shoud make them funnny
    '''
    t = 0
    for i in range(len(bs)):
        for j in range(i+1, len(bs)):
            #Finding union of the two bodies
            u = len(d[bs[i]].union(d[bs[j]]))
            '''
            Since a body cannot be headed by a letter such that concatenation of them is a 
            funny word, we remove such letters from the union.
            nb1 = number of heads body b1 can choose, so that their concatenation is not funny
            nb2 = number of heads body b2 can choose, so that their concatenation is not funny
            Since we need to find total number of such pairs possible,
            the total number of pairs formed when body b1 and body b2 are used is
            nb1*nb2
            Similarly we iterate over all bs(unique values of body availble)
            to calcualte the total number of pairs possible over all values of bodies!
            '''
            nb1 = (u-len(d[bs[i]]))
            nb2 = (u-len(d[bs[j]]))
            t += nb1*nb2
    '''
    We finally multiply the answer by two, since each valid pair can be altered in position
    to form its reverse, which is also a valid pair
    '''
    print(2*t)

