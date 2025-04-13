for _ in range(int(input())):
    n, k, x = map(int, input().split())
    a = 2 ** (k - 1)
    if x < a:
        print("No")
    else:
        print("Yes")
