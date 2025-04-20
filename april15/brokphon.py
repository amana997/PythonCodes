for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = []
    for i in range(n - 1):
        if a[i] != a[i + 1]:
            s.append(i)
            s.append(i + 1)
    print(len(set(s)))
