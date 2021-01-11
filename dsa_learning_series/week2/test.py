for _ in range(int(input())):
    n = int(input())
    l = input()
    stack = []
    o = {'^':3, '*':2, '/':2, '+':1, '-':1, '(':0, ')':0}
    output = []

    for i in l:
        if i=='(':
                stack.append(i)
        elif i==')':
            p = stack.pop()
            while p!='(':
                output.append(p)
                p = stack.pop()
                if len(stack)==0:
                    break
        elif i in o.keys():
            if len(stack)==0:
                stack.append(i)
            else:
                m = o[stack[-1]]
                pr = o[i]
                if pr>m:
                    stack.append(i)
                else:
                    p = stack.pop()
                    while o[p]>=pr:
                        output.append(p)
                        p=stack.pop()
        else:
            output.append(i)
    print(output+stack)
