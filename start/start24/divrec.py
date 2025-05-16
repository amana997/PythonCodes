for _ in range(int(input())):
    x, a, b = map(int, input().split())
    
    if x == a:
        print(b)
    elif a <= b:
        print(-1)
    else:
        n = x // a * b
        print(n)
