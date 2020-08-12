def beautifulArray(self ,N):
    res = [1]
    while len(res) < N:
        res = [i * 2 - 1 for i in res] + [i * 2 for i in res]
    return [i for i in res if i <= N]
  
 
def swap(l, p1, p2): 
	
	l[p1], l[p2] = l[p2], l[p1] 
	return l  
    
n,k = map(int, input().split())
 
a = []
for i in range(1,n+1):
    a.append(i)
    
if n==1 and k==1:
    print("Yes")
    print(1)
    
elif n==k:
    print("Yes")
    for i in range(1,n+1):
        print(i,end=" ")
if n > k:        
    if n>1 and k==1:
        print("No")
    elif n>1 and k==2:
        print("Yes")
        for i in beautifulArray(1,n):
            print(i, end=" ")
    else:
        m = []
        y = []
        z = []
        
        # print(a[-1])
        
        # print(swap(a, a[k-1]-1, a[-1]-1)) 
        x = swap(a, a[k-1]-1, a[-1]-1)
        
        #print(beautifulArray(1,n))
        m = beautifulArray(1,n-k-1)
        
        for i in m:
            y.append(i+k)
        
        # print(y)
        # print(x)
        
        for i in range(k):
            z.append(x[i])
        for i in range(n-k-1):
            z.append(y[i])
        z.append(x[-1])
        
        print("Yes")
        for i in z:
            print(i,end=" ")