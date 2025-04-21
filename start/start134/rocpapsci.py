for _ in range(int(input())):
    n = int(input())
    s = input()
    
    c = n - s.count('RR') - s.count('PP') - s.count('SS')
        
    print(c)
