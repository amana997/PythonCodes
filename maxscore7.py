for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    i = 0
    j = len(a) - 1
    s = 0
    
    while i < j:
        s += abs(a[j] - a[i])
        i += 1
        j -= 1
    print(s)
