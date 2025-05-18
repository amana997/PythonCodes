def xor(a, n):
    x = a[0]
    for i in range(1, n):
        x ^= a[i]
    
    return x

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    if n % 2 == 1:
        print("YES")
    else:
        if xor(a, n) == 0:
            print("YES")
        else:
            print("NO")
