for _ in range(int(input())):
    n = int(input())
    s = str(input())
    ans = 0
    balance = 0
    for i in range(1, n, 2):
        if s[i] == '0':
            balance -= 1
        else:
            balance += 1
        if s[i - 1] == '0':
            balance -= 1
        else:
            balance += 1
        if balance == 0:
            ans += 1
    ans = 2 ** ans
    print(ans)
