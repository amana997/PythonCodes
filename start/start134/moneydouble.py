for _ in range(int(input())):
    x, y = map(int, input().split())
    if x < 1000:
        x += 1000
        y -= 1
    
    ans = x * (2 ** y)
    print(ans)
