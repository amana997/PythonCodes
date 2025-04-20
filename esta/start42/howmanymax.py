for _ in range(int(input())):
    n = int(input())
    s = str(input())
    node = ""
    vertice = ""
    
    for i in s:
        if(vertice != i):
            node += i
            vertice = i
    
    if node == "0" or node == "1":
        print(1)
    else:
        ans = node.count("01")
        
        if node[0] == "1":
            ans += 1
        if node[-1] == "0":
            ans += 1
        print(ans)
