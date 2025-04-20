d1, v1, d2, v2, p = map(int, input().split())
day = 0
vac = 0

while vac < p:
    day += 1
    if d1 <= day:
        vac += v1
    if d2 <= day:
        vac += v2

print(day)
