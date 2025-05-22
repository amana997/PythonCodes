for _ in range(int(input())):
    n, m, h = map(int,input().split())
    c = list(map(int, input().split()))
    p = list(map(int, input().split()))
    
    min_nm = min(n ,m)
    
    c.sort(reverse = True)
    p.sort(reverse = True)
    
    ans = 0
    for i in range(min_nm):
        if c[i] < (p[i] * h):
            ans += c[i]
        else:
            ans += p[i] * h
    
    print(ans)
