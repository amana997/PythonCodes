for _ in range(int(input())):
    n = int(input())
    
    a = [[0] * n for i in range(n)]
    b = 1
    for i in range(n):
        for j in range(n):
            a[i][j] = b
            b += 1
    
    if n % 2 == 0:
        if n == 2:
            print(-1)
            continue
        a[1][1], a[1][2] = a[1][2], a[1][1]
        a[2][0], a[2][1] = a[2][1], a[2][0]
    else:
        r = 1
        c = 1
        while r < n - 1 and c < n:
            a[r][c], a[r][c + 1] = a[r][c + 1], a[r][c]
            r += 1
            c += 2
    for i in a:
        print(*i)
