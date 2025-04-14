for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    
    f1 = {}
    f2 = {}
    f3 = {}
    f4 = {}
    
    for i in range(n):
        for j in range(m):
            if a[i][j] - i - j not in f1:
                f1[a[i][j] - i - j] = 1
            else:
                f1[a[i][j] - i - j] += 1
            if a[i][j] - i + j not in f2:
                f2[a[i][j] - i + j] = 1
            else:
                f2[a[i][j] - i + j] += 1
            if a[i][j] + i - j not in f3:
                f3[a[i][j] + i - j] = 1
            else:
                f3[a[i][j] + i - j] += 1
            if a[i][j] + i + j not in f4:
                f4[a[i][j] + i + j] = 1
            else:
                f4[a[i][j] + i + j] += 1
                
    c1 = (n * m) - max(f1.values())
    c2 = (n * m) - max(f2.values())
    c3 = (n * m) - max(f3.values())
    c4 = (n * m) - max(f4.values())
    ans = min(c1, c2, c3, c4)
    print(ans)
