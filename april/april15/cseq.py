mod = 10 ** 6 + 3
fact = [1] * mod
factinv = [1] * mod
for i in range(1, mod):
    fact[i] = (fact[i - 1] * i) % mod
    factinv[i] = pow(fact[i], -1, mod)

for _ in range(int(input())):
    n, l, r = map(int, input().split())
    a = n + r - l + 1
    ans = 1
    while n > 0:
        i, j = a % mod, n % mod
        if i >= j:
            ans = (ans * fact[i] * factinv[j] * factinv[i - j]) % mod
        else:
            ans = mod
            break
        a //= mod
        n //= mod
    
    print(ans - 1)
