for _ in range(int(input())):
    n, k, v = map(int, input().split())
    a = list(map(int, input().split()))
    
    num = (n + k) * v
    for i in a:
        num -= i
    
    if (num > 0) and (num % k == 0):
        print(num // k)
    else:
        print(-1)
    
