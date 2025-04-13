for _ in range(int(input())):
    n = int(input())
    a = str(input())
    b = str(input())
    score = 0
    flag = 0
    
    for i in range(n):
        if a[i] == "1" and b[i] == "1":
            score += 1
        elif a[i] == "1" or b[i] == "1":
            flag = 1
            break
    
    if flag == 1 or score % 2 == 1:
        print("YES")
    else:
        print("NO")
