def f(s):
    balance = 0
    max_balance = 0
    for i in range(len(s)):
        if s[i] == "(":
            balance += 1
        if s[i] == ")":
            balance -= 1
        max_balance = max(max_balance, balance)
    return max_balance

for _ in range(int(input())):
    s = str(input())
    a = f(s)
    print("(" * a, end = "")
    print(")" * a)
