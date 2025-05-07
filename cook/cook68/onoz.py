def solve(h, m):
    count = 0
    for i in range(h):
        s_i = str(i)
        if all(c == s_i[0] for c in s_i):
            for j in range(m):
                s_j = str(j)
                if all(c == s_j[0] for c in s_j) and (s_i[0] == s_j[0]):
                    count += 1
    print(count)

t = int(input())
for _ in range(t):
    h, m = map(int, input().split())
    solve(h, m)
