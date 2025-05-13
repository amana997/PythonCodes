MAXN = 10**6

divisors = [0] * (MAXN + 1)
for i in range(1, MAXN + 1):
    for j in range(i, MAXN + 1, i):
        divisors[j] += 1

valid_divisors = set()
for i in range(1, MAXN + 1):
    if divisors[i] == 4:
        valid_divisors.add(i)

min_divisors = divisors[:]

for i in range(1, MAXN + 1):
    for j in range(i, MAXN + 1, i):
        if i in valid_divisors:
            min_divisors[j] = min(min_divisors[j], min_divisors[j // i])

for _ in range(int(input())):
    n = int(input())
    print(min_divisors[n])
