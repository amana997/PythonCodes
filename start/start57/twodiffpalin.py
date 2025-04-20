for _ in range(int(input())):
    a, b = map(int, input().split())
    
    if a < 2 or b < 2:
        print("NO")
    elif a % 2 == 0 or b % 2 == 0:
        print("YES")
    else:
        print("NO")
