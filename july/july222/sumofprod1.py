for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    count = 1
    for i in a:
        if i == 0:
            count = 1
        else:
            ans += count
            count += 1
    print(ans)
