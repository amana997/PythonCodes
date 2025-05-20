for _ in range(int(input())):
    n = int(input())
    
    if n <= 3:
        print("BRONZE")
    elif n <= 6:
        print("SILVER")
    else:
        print("GOLD")
