for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    max_val = a[0]
    for i in range(1, n):
        if a[i] < max_val:
            ans += 1
        else:
            max_val = a[i]
    
    print(ans)
