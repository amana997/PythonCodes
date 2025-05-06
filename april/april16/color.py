for _ in range(int(input())):
    n = int(input())
    s = input()
    a = []
    a.append(s.count('R'))
    a.append(s.count('G'))
    a.append(s.count('B'))
    
    print(n - max(a))
