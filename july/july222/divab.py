for _ in range(int(input())):
    a, b, n = map(int, input().split())
    r = n - (n % a)
    if a % b == 0:
        print(-1)
    else:
        if n % a != 0:
            r += a
        if r % b == 0:
            r += a
        print(r)
