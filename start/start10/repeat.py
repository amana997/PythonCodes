for _ in range(int(input())):
    n, k, s = map(int, input().split())
    
    ans = (s - (n ** 2)) // (k - 1)
    print(ans)
