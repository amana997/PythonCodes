for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    sorted_a = sorted(a)
    i = 0
    l = 0
    for idx in range(n):
        if sorted_a[i] == a[idx]:
            i += 1 
        else:
            if a[idx] < l:
                print("NO")
                break
            l = a[idx]
    else:
        print("YES")
