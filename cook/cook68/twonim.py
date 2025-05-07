for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    val = 0
    for i in a:
        val ^= i
    
    if val == 0:
        print("First")
    else:
        if n % 2 == 0:
            print("First")
        else:
            print("Second")
