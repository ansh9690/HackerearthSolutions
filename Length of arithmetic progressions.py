n,q = map(int, input().split())
a = [int(x) for x in input().split()]

while q!=0:
    count=0
    l,r,d = map(int, input().split())
    if l!=r:
        for i in range(l-1,r-1):
            dif=a[i+1]-a[i]
            if dif == d:
                count=count+1
        print(count+1)
        
    else:
        print(1)
    q=q-1