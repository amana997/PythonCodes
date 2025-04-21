for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    count = 1
    a = []
    for i in range(n - 1):
        if(x[i + 1] - x[i] <= 2):
            count += 1
        else:
            a.append(count)
            count = 1
    a.append(count)
    print(min(a), max(a))
