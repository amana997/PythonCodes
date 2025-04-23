for _ in range(int(input())):
    s = sorted(input())
    l = len(s)
    p = 0
    for i in range(l):
        p += (i + 1) * (ord(s[i]) - 96)
    
    print(p)
