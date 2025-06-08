for _ in range(int(input())):
    n, l = map(int, input().split())
    
    if l >= 2000:
        for i in range(n):
            print(i + 1, end = " ")
        print()
    else:
        ans = 1
        for i in range(n):
            print(ans, end = " ")
            ans += l
        print()
