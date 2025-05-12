from math import ceil

for _ in range(int(input())):
    n, x = map(int, input().split())
    a = (n * x) / 4
    print(ceil(a))
