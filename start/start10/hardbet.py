for _ in range(int(input())):
    a = list(map(int, input().split()))
    m = min(a)
    
    if a[0] == m:
        print("Draw")
    elif a[1] == m:
        print("Bob")
    else:
        print("Alice")
