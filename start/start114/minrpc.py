for _ in range(int(input())):
    n = int(input())
    a = input()
    l = n // 2 + 1
    for i in range(n):
        if a[i] == "R":
            l -= 1
    
    s = ["P"] * n
    for i in range(n - 1, -1, -1):
        if l > 0 and a[i] != "R":
            if a[i] == "P":
                s[i] = "S"
            else:
                s[i] = "R"
            l -= 1
        
    print("".join(s))
