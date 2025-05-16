for _ in range(int(input())):
    x = int(input())
    
    a = x
    b = x + (1 << 27)
    c = x + (1 << 28)
    
    print(a, b, c)
