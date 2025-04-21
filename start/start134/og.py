for _ in range(int(input())):
    n = int(input())
    x = n // 9
    r = n % 9
    ans = x * 45 + ((r + 1) * r) // 2
    
    print(ans)
