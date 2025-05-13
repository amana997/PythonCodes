for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    
    neg = (a[1] - 1) * (a[0] + 1)
    neg += 1
    pos = (a[-1] - 1) * (a[-2] + 1)
    pos += 1
    
    print(max(neg, pos))
