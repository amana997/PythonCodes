from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    
    if a == b:
        print("Yes")
        continue
    
    possible = True
    for i in range(n):
        if (a[i] == "b" and b[i] != "b") or (a[i] != "b" and b[i] == "b"):
            possible = False
            break
    
    if not possible:
        print("No")
        continue
    
    naa = a.count("a")
    nab = b.count("a")
    if naa != nab:
        print("No")
        continue
    
    ac = []
    
    for i in range(n):
        if a[i] == "a" and b[i] == "c":
            ac.append(i)
        elif a[i] == "c" and b[i] == "a":
            if not ac:
                possible = False
                break
            elif not "b" in a[ac[0]: i]:
                possible = False
                break
            else:
                ac.pop(0)
    
    if possible:
        print("Yes")
    else:
        print("No")
