for _ in range(int(input())):
    n = int(input())
    s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(n):
        a = list(input())
        for j in range(10):
            s[j] = s[j] ^ int(a[j])
    
    print(s.count(1))
