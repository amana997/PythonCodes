for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    flag = True
    for i in range(1, n):
        if b[i - 1] % b[i] != 0:
            flag = False
            break
    
    if flag:
        print(*b)
    else:
        print(-1)
