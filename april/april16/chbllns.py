for _ in range(int(input())):
    balls = list(map(int, input().split()))
    k = int(input())
    ans = 0
    
    for color in balls:
        if color < k:
            ans += color
        else:
            ans += k - 1
    
    print(ans + 1)
