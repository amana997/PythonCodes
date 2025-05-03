def algo1(a):
    n = len(a)
    if n == 1:
        return a
    while n > 1:
        s = []
        if n % 2 == 1:
            a.pop()
            n -= 1
            while n > 0:
                s.append(a.pop())
                a.pop()
                n -= 2
        else:
            while n > 0:
                a.pop()
                s.append(a.pop())
                n -= 2
        
        num = int(input())
        if len(s) != 1 and num == 1:
            return algo1(s)
        elif len(s) != 1 and num == 0:
            return algo2(s)
        else:
            return s
        
def algo2(a):
    n = len(a)
    if n == 1:
        return a
    while n > 1:
        s = []
        if n % 2 == 1:
            s.append(a.pop())
            n -= 1
            while n > 0:
                a.pop()
                s.append(a.pop())
                n -= 2
        else:
            while n > 0:
                s.append(a.pop())
                a.pop()
                n -= 2
        
        num = int(input())
        if len(s) != 1 and num == 1:
            return algo1(s)
        elif len(s) != 1 and num == 0:
            return algo2(s)
        else:
            return s
        
a = [i for i in range(52)]
if int(input()) == 1:
    a = algo1(a)
else:
    a = algo2(a)

ans = 52 - a[0]
print(ans)
