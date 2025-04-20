for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = -n
    for i in range(n):
        ans += a[i]
    
    print(ans)
