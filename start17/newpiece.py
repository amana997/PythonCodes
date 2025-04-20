for _ in range(int(input())):
    a, b, p, q = map(int, input().split())
    
    if a == p and b == q:
        print(0)
    else:
        n = a + b - p - q
        if n % 2 == 0:
            print(2)
        else:
            print(1)
