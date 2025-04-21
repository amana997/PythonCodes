for _ in range(int(input())):
    delivery, coupon = map(int, input().split())
    a, b, c = map(int, input().split())
    x, y, z = map(int, input().split())
    total = 0
    
    if a + b + c >= 150:
        total += delivery
    if x + y + z >= 150:
        total += delivery
    
    if coupon < total:
        print("YES")
    else:
        print("NO")
