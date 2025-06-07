from math import ceil

for _ in range(int(input())):
    a, b = map(int, input().split())
    
    r = 10 - a + b
    
    if r <= 0:
        print(0)
    else:
        ans = ceil(r / 3)
        print(ans)
