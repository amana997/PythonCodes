for _ in range(int(input())):
    n, m = map(int, input().split())
    s = n
    a = [n, n]
    max_diff = 0
    while s <= (n * 2) and s <= m:
        r = m % s
        num = m - r
        if abs(num - s) > max_diff:
            max_diff = abs(num - s)
            a = [s, num]
        s += 1
    print(*a)
