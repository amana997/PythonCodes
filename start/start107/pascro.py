for _ in range(int(input())):
    n = int(input())
    A = input()
    B = input()
    
    a = b = 0
    
    for i in range(n):
        if A[i] == 'R' and B[i] == 'P':
            b += 1
        elif A[i] == 'R' and B[i] == 'S':
            a += 1
        elif A[i] == 'P' and B[i] == 'S':
            b += 1
        elif A[i] == 'P' and B[i] == 'R':
            a += 1
        elif A[i] == 'S' and B[i] == 'R':
            b += 1
        elif A[i] == 'S' and B[i] == 'P':
            a += 1
    
    if a > b:
        print(0)
    elif a == b:
        print(1)
    else:
        print(abs(a - b) // 2 + 1)