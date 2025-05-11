def comb(n, k):
    return factorial[n] / (factorial[n - k] * factorial[k])

factorial = [1] * 1001
for i in range(1, 1001):
    factorial[i] = factorial[i - 1] * i

for _ in range(int(input())):
    s, n, m, k = map(int, input().split())
    prob = 0
    
    for i in range(k, min(m, n)):
        prob += comb(m - 1, i) * comb(s - m, n - i - 1)
    total = comb(s - 1, n - 1)
    ans = float(prob / total)
    
    print(f"{ans:.6f}")
