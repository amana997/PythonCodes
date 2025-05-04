from math import sqrt

for _ in range(int(input())):
    n = int(input())
    ans = 0
    root = int(sqrt(n)) + 1
    for i in range(1, root):
        if n % i == 0:
            ans += i
            if i * i != n:
                ans += n // i
    print(ans)
