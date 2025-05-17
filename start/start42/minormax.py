for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    flag = 0
    mi = ma = a[0]
    for i in range(1, n):
        if a[i] <= mi:
            mi = a[i]
        elif a[i] >= ma:
            ma = a[i]
        else:
            flag = 1
            break
    
    if flag == 0:
        print("YES")
    else:
        print("NO")
