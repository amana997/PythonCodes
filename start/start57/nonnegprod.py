for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    if 0 in a:
        print(0)
        continue
    for i in a:
        if i < 0:
            count += 1
    
    if count % 2 == 1:
        print(1)
    else:
        print(0)
        
