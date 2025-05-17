for _ in range(int(input())):
    n, k = map(int, input().split())
    
    ans = [0] * 30
    ans[0] = k
    
    for i in range(30):
        if ans[i] >= n:
            a = (ans[i] - n + 1) // 2
            ans[i + 1] += a
            ans[i] -= 2 * a
        else:
            break
    print(sum(ans))
