def isPrime(n) : 
  
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

count = 0  
n = int(input())
a = [int(x) for x in input().split()]
  
for i in range(n):
    if(isPrime(a[i])):
        count=count+1
        
print(count+1)
    