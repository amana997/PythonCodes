n = int(input())
a = []
for i in range(n):
    s = input()
    a. append(s)
a.reverse()
b = list(dict.fromkeys(a))
ans = ""
for i in b:
    ans += i[-2:]

print(ans)
