n, k = map(int, input().split())

mod = 10 ** 9 + 7

if n == 1 and k == 1:
    print(1)
elif n == 1:
    print(0)
else:
    a = pow(k * n, n - 2, mod)
    b = pow(k * n - k, (k - 1) * n, mod)
    ans = (a * b) % mod
    print(ans)
