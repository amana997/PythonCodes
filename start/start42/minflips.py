for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    if n % 2 == 1:
        print(-1)
    else:
        b = a.count(1)
        c = a.count(-1)
        ans = abs(b - c) // 2
        print(ans)
