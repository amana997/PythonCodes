for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    total = 0
    for i in a:
        total += i
    
    if total % 2 == 0:
        print("Yes")
    else:
        print("No")