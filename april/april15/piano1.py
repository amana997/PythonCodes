for _ in range(int(input())):
    p = input()
    n = int(input())
    
    length = 0
    for i in range(len(p)):
        if p[i] == 'T':
            length += 2
        elif p[i] == 'S':
            length += 1
    
    size = n * 12
    count = 0
    
    for i in range(size):
        count += (size - i - 1) // length
    
    print(count)
