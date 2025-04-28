for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    ans.append(a[0] & a[1])
    for i in range(1, n - 1):
        m = max(a[i] & a[i + 1], a[i] & a[i - 1])
        ans.append(m)
    ans.append(a[-1] & a[-2])
    print(*ans)
