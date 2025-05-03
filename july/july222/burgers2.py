for _ in range(int(input())):
    x, y, n, r = map(int, input().split())
    dif = y - x
    if r // x < n:
        print(-1)
    else:
        r -= x * n
        if r // dif > n:
            b = n
        else:
            b = r // dif
        a = n - b
        print(a, b)
