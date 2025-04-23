for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    a.sort()
    for i in range(n):
        if ans >= a[i]:
            ans += 1
    
    print(ans)
