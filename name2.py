def sub(a, b):
    l1 = len(a)
    l2 = len(b)
    i = 0
    j = 0
    
    while i < l1 and j < l2:
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i == l1:
        return "YES"
    else:
        return "NO"


for _ in range(int(input())):
    m, w = map(str, input().split())
    
    if len(m) > len(w):
        print(sub(w, m))
    else:
        print(sub(m, w))
