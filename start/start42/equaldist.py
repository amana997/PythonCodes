for _ in range(int(input())):
    a, b = map(int, input().split())
    
    ans = (a + b) % 2
    
    if ans == 0:
        print("YES")
    else:
        print("NO")
