a = [0]
d = {}
d[0] = [0]

for i in range(1, 128):
    x = a[i - 1]
    l = len(d[x])
    
    if l == 1:
        a.append(0)
        d[0].append(i)
    else:
        dif = d[x][-1] - d[x][-2]
        a.append(dif)
        if dif not in d:
            d[dif] = [i]
        else:
            d[dif].append(i)

for _ in range(int(input())):
    n = int(input())
    
    ans = a[:n].count(a[n - 1])
    print(ans)
