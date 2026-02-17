for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    d = 100
    index = 100
    for i in range(n):
        if a[i] - b[i] < d:
            d = a[i] - b[i]
            index = i
    
    ans = 0
    for i in range(n):
        if index == i:
            ans += b[i]
        else:
            ans += a[i]
    
    print(ans)