for _ in range(int(input())):
    a, b, x, y = map(int, input().split())
    chef = a / x
    chefina = b / y
    
    if chefina == chef:
        print("Both")
    elif chef < chefina:
        print("Chef")
    else:
        print("Chefina")
