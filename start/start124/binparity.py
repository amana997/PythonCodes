for _ in range(int(input())):
    n = int(input())
    count = 0
    while n > 0:
        count += n % 2
        n //= 2
    
    if count % 2 == 0:
        print("EVEN")
    else:
        print("ODD")
