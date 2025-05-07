for _ in range(int(input())):
    n, k = map(int, input().split())
    
    print((k*pow(k-1,n-1,1000000007))%1000000007)
