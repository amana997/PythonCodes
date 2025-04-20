for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a.count(0) == n:
        print(-1)
    elif a[n - 1] <= 0:
        print(a[0], a[0])
    else:
        print(a[-1], a[-1])
