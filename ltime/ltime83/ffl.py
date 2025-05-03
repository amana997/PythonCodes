for _ in range(int(input())):
    n, s = map(int, input().split())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    budget = 100 - s
    defender, forward = [], []
    for i in range(n):
        if a[i] == 0:
            defender.append(p[i])
        elif a[i] == 1:
            forward.append(p[i])
    
    if len(defender) == 0 or len(forward) == 0:
        print("no")
    else:
        if min(forward) + min(defender) <= budget:
            print("yes")
        else:
            print("no")
