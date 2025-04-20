for _ in range(int(input())):
    n, u, d = map(int, input().split())
    h = list(map(int, input().split()))
    flag = True
    i = 1
    while i < n:
        if h[i] - h[i - 1] > 0 and h[i] - h[i - 1] <= u:
            i += 1
        elif h[i - 1] - h[i] > 0 and h[i - 1] - h[i] <= d:
            i += 1
        elif h[i - 1] - h[i] > 0 and flag:
            flag = False
            i += 1
        elif h[i] == h[i - 1]:
            i += 1
        else:
            break
    
    print(i)
