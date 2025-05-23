for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    b = len(bin(max(a)))
    c = len([i for i in a if len(bin(i)) == b])
    
    if c % 2 == 0:
        print(c // 2)
    else:
        print((c // 2) + 1)
