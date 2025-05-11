for _ in range(int(input())):
    n, q = map(int, input().split())
    s = input()
    a = {}
    
    for i in s:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1
    
    for i in range(q):
        ans = 0
        c = int(input())
        for j in a:
            if a[j] > c:
                ans += a[j] - c
        print(ans)
