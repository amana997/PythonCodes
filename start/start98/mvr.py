a, b, x, y = map(int,input().split())

c = 2 * a + b
z = 2 * x + y

if c > z:
    print("Messi")
elif c < z:
    print("Ronaldo")
else:
    print("Equal")
