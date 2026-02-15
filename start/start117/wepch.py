import math

for _ in range(int(input())):
    h, x, y1, y2, k = map(int, input().split())
    
    gun = math.ceil(h / x)
    
    r = h - (k * y1)
    if r <= 0:
        laser = math.ceil(h / y1)
    else:
        laser = k + math.ceil(r / y2)
    
    print(min(gun, laser))