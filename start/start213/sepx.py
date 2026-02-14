for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    
    if x in a:
        print("Yes")
    elif x > max(a) or x < min(a):
        print("Yes")
    else:
        print("No")