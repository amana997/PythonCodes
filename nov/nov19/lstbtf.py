import math
extras=[[]]
curr=1
while curr<4500:
    poss=[]
    p=100
    for x in range(2,10):
        t=curr+1-x*x
        if t>=0:
            if extras[t]!=-1:
                a=extras[t].copy()
                a.append(x-1)
                if len(a)==p:
                    a.sort()
                    if a<poss:
                        poss=a
                elif len(a)<p:
                    p=len(a)
                    poss=a
                    poss.sort()
    if poss==[]:
        extras.append(-1)
    else:
        extras.append(poss)
    curr+=1

def ltoi(lis):
    res=0
    for x in lis:
        res*=10
        res+=x
    return res

for x in range(int(input())):
    n=int(input())
    m=math.ceil(math.sqrt(n))
    t=-1
    while m**2-n<4000:
        if extras[m**2-n]==-1:
            m+=1
        else:
            if t==-1 or ltoi(extras[m**2-n])<t:
                t=ltoi(extras[m**2-n])
            m+=1
    z=str(t)
    l=len(z)
    y=str(int("1"*l)+t)
    b='1'*(n-l)+y
    print(b)
