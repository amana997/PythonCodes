from collections import Counter

for _ in range(int(input())):
    s = input()
    n = len(s)
    
    d = Counter(s)
    charset = set(d.keys())
    
    moves = n
    
    for c in charset:
        substr = s[0:d[c]]
        count = substr.count(c)
        moves = min(moves, d[c] - count)
        
        l = 0
        r = d[c] - 1
        while r + 1 < n:
            l += 1
            r += 1
            
            if s[l - 1] == c:
                count -= 1
            if s[r] == c:
                count += 1
            
            moves = min(moves, d[c] - count)
    
    print(moves)
