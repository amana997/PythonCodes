for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    first = a[0]
    module_inversions = 0
    for i in range(1, n):
        if abs(a[i]) != abs(a[i-1]):
            module_inversions = 2
            break
        elif a[i] != a[i-1]:
            module_inversions += 1
    if module_inversions > 1:
        print("No")
    else:
        print("Yes")