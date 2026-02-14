for _ in range(int(input())):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    
    ans = -1
    move = k
    
    for i in p:
        if i > k:
            continue
        elif k % i == 0:
            m = (k - i) // i
            if move > m:
                move = m
                ans = i
    
    print(ans)