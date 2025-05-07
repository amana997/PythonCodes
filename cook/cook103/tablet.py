for _ in range(int(input())):
    n, b = map(int, input().split())
    a = 0
    for i in range(n):
        w, h, p = map(int, input().split())
        
        if a < w * h and p <= b:
            a = w * h
    
    if a == 0:
        print("no tablet")
    else:
        print(a)
