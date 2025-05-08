def dic(a):
    d = {}
    for i in range(len(a)):
        if a[i] not in d:
            d[a[i]] = {i}
        else:
            d[a[i]].add(i)
    return d

def solve(a, k):
    d = dic(a)
    
    c = sorted(a)
    for i in range(len(c)):
        if c[i] != a[i]:
            flag = 0
            for j in d[c[i]]:
                if abs(j - i) % k == 0:
                    flag = 1
                    break
            if flag == 0:
                return "no"
    return "yes"

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    if k == 1:
        print("yes")
    else:
        print(solve(a, k))
