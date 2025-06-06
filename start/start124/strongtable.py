for _ in range(int(input())):
    n = int(input())
    w = list(map(int, input().split()))
    w.sort()
    max_w = 0
    for i in range(n):
        legs = n - i
        if max_w < (legs * w[i]):
            max_w = legs * w[i]
    
    print(max_w)
