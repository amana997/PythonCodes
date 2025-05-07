for _ in range(int(input())):
    n, m = map(int, input().split())
    
    if n == 1 or m == 1:
        if n == 2 or m == 2:
            print("Yes")
        else:
            print("No")
    elif n % 2 == 0 or m % 2 == 0:
        print("Yes")
    else:
        print("No")
