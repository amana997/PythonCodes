for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    
    if n == 4:
        if a[0] + a[1] == a[2] + a[3]:
            print("NO")
        else:
            print("YES")
    else:
        s = set(a)
        if len(s) == 1:
            print("NO")
        else:
            print("YES")
