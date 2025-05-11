for _ in range(int(input())):
    a, b = input().split()
    n=int(input())
    parent = {}
    child = {}
    flag = 0
    for i in a:
        if i not in parent:
            parent[i] = 1
        else:
            parent[i] += 1
    for i in b:
        if i not in parent:
            parent[i] = 1
        else:
            parent[i] += 1
    s = ""
    for i in range(n):
        s += input()
        
    for i in s:
        if i not in child:
            child[i] = 1
        else:
            child[i] += 1
        
        if i not in parent:
            flag = 1
            break
        elif child[i] > parent[i]:
            flag = 1
            break
    
    if flag == 1:
        print("NO")
    else:
        print("YES")
