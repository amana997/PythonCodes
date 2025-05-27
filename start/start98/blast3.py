for _ in range(int(input())):
    n = int(input())
    s = input()
    flag = set()
    if n % 3 == 1:
        print('YES')
    else:
        for i in range(n):
            if i % 3 == 0:
                flag.add(s[i])
            else:
                if (n - i - 1) % 3 == 0 and s[i] in flag:
                    print('YES')
                    break
        else:
            print('NO')
