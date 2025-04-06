for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = a + b
    d = {}
    for i in c:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1
    r=0
    for i in d:
        if d[i] > r:
            r = d[i]
    print(r)
