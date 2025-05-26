for _ in range(int(input())):
    n, m = map(int,input().split())
    a = list(map(int, input().split()))
    
    total = sum(a)
    b = n * m
    
    if total < b - n:
        print(0)
    else:
        print(n - b + total)
