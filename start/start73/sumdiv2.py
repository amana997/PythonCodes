for _ in range(int(input())):
    x, y = map(int,input().split())
    if x == y:
        print(x)
    elif x == 1 or y == 1:
        print(max(x, y) - 1)
    else:
        a = (x * y) - x - y
        print(a)
