for _ in range(int(input())):
    x, y, z = map(int, input().split())
    
    ans = z // (x * y * 2)
    print(ans)
