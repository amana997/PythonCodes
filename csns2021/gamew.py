for _ in range(int(input())):
    n = int(input())
    s = input()
    c = s.count('01') + s.count('10') + 1
    
    if c % 3 == 2:
        print("RAMADHIR")
    else:
        print("SAHID")
