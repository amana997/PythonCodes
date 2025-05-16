for _ in range(int(input())):
    x, y = map(int, input().split())
    
    if x == y:
        ans = y + x - 1
    else:
        ans = y + x
    
    print(ans)
