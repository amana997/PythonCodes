from math import ceil

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int,input().split()))
    
    k = sum(a)
    ma = max(a)
    mi = min(a)
    t = ma * n
    d = t - k
    print(max((ma - mi), ceil(d/m)))
