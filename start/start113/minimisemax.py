for _ in range(int(input())):
    x, y = map(int, input().split())
    
    a = x // (y + 1)
    if x % (y + 1):
        a += 1
    print(max(a, (-2) * y + x))
