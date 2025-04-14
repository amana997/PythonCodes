for _ in range(int(input())):
    a = int(input())
    profit = 0
    max_profit = 0
    day = 0
    day2 = 0
    while True:
        day_profit = a - (2 ** day)
        profit += day_profit
        
        if max_profit < profit:
            day2 = day + 1
            max_profit = profit
        
        if profit < 0:
            break
        else:
            day += 1
    
    print(day, day2)
