from math import comb
a = []
def sol(seats):
    for j in range(9):
        compartment = seats[4 * j: 4 * j + 4] + seats[53 - 2 * j] + seats[52 - 2 * j]
        a.append(compartment)
    
x, n = map(int, input().split())
ans = 0
for i in range(n):
    seats = input()
    sol(seats)

for seat in a:
    zero = seat.count('0')
    if zero < x:
        continue
    else:
        ans += comb(zero, x)

print(ans)
