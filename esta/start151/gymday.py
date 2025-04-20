for _ in range(int(input())):
    d, x, y = map(int, input().split())
    ans = -1
    if y >= x:
        print(0)
    else:
        c = 0
        while y != 0:
            c += 1
            y -= 1
            discount = (d * c * x) / 100
            p = x - discount
            if y >= p:
                ans = c
                break
        print(ans)
