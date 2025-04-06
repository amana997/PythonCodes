for _ in range(int(input())):
    n, y = map(int, input().split())
    a = list(map(int,input().split()))
    bor = 0
    for i in a:
        bor = bor | i
    x=bor^y
    if x | bor == y:
        print(x)
    else:
        print(-1)
