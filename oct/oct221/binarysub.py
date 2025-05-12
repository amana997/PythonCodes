mod = 998244353
for _ in range(int(input())):
    s = input()
    n = len(s)
    
    a = [1] * n
    if n == 1:
        print(a[0])
    else:
        if s[0] != s[1]:
            a[1] = 2
        for i in range(2, n):
            if s[i] == s[i - 1]:
                a[i] = a[i - 1]
            else:
                a[i] = (a[i - 1] + a[i - 2]) % mod
        print(a[n - 1])
