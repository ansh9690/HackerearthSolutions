n,m = map(int, input().split())


def fun(n):
    x=1
    for i in range(1,n+1):
        x=(x*i)%1000000007
    
    return x
    
print(fun(m))