for _ in range(int(input())):
    n = int(input())
    s = input()
    
    idx = []
    for i in range(n):
        if s[i] == s[0]:
            idx.append(i)
    l = len(idx)
    
    if l == 1:
        print(s)
        continue
    
    for i in range(0, idx[1] + 1):
        for j in range(l):
            if n <= idx[j] + i:
                break
            if s[idx[j] + i] != s[i]:
                break
        else:
            continue
        break
    print(s[:i])
