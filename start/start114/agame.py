for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    odd = even = 0
    for i in range(n):
        if i % 2:
            odd += a[i]
        else:
            even += a[i]
    
    if n == 1:
        if even == 1:
            print("Bob")
        else:
            print("Alice")
    else:
        if odd % 2 and even % 2:
            if ((odd + even) // 2) % 2 == 0:
                print("Alice")
            else:
                print("Bob")
        elif odd % 2 == 0 and even % 2 == 0:
            if ((odd + even) // 2) % 2 == 0:
                print("Bob")
            else:
                print("Alice")
        else:
            print("Bob")
