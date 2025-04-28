for _ in range(int(input())):
    a, b, c, p, q, r = map(int, input().split())
    ans1 = a + b + r
    ans2 = a + q + c
    ans3 = p + b + c
    ans = max(ans1, ans2, ans3)
    half = (p + q + r) / 2
    
    if ans > half:
        print("YES")
    else:
        print("NO")
