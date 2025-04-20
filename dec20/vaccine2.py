import math

for _ in range(int(input())):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    
    risk = 0
    norisk = 0
    for i in a:
        if i <=9 or i>=80:
            risk += 1
        else:
            norisk += 1
    
    days = math.ceil(risk / d) + math.ceil(norisk / d)
    print(days)
