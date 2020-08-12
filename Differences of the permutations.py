t = int(input())
while t!=0:
    n = int(input())
    
    m = 1
    for i in range(1,n+1):
        m = m*i
    x = (n**2-n)//2
    y = m*x
    print(y)
    t=t-1