for _ in range(int(input())):
    n = int(input())
    blood = list(map(str, input().split()))
    a = blood.count("A")
    b = blood.count("B")
    ab = blood.count("AB")
    o = blood.count("O")
    
    print(max((a + ab + o), (b + ab + o)))
