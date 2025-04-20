for _ in range(int(input())):
    n, k = map(int, input().split())
    k = n - k
    a = []
    for i in range(1, n + 1):
        if(i % 2 != 0 and k > 0):
            a.append(-i)
            k -= 1
        else:
            a.append(i)
    if k != 0:
        for i in range(n, 0, -1):
            if i % 2 == 0 and k != 0:
                a[i - 1] *= -1
                k -= 1
    
    print(*a)
