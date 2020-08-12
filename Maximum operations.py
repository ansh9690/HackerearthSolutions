import math 

def myXOR(x, y): 
	return ((x | y) & 
			(~x | ~y)) 

def swap(a,b): 
	temp=a 
	a=b 
	b=temp 
	
def myXNOR(a, b): 
	if (a < b): 
		swap(a, b) 
	if (a == 0 and b == 0) : 
		return 1; 
	a_rem = 0
	b_rem = 0
	count = 0
	xnornum = 0
	while (a!=0) : 
		a_rem = a & 1
		b_rem = b & 1
		if (a_rem == b_rem):	 
			xnornum |= (1 << count) 
		count=count+1
		
		a = a >> 1
		b = b >> 1
	
	return xnornum; 
t=int(input())
while t!=0:
    a,b,n = map(int, input().split())
    x = myXOR(a,b)
    y = myXNOR(a,b)

    if n%3 == 0:
        if x>y:
            print(x)
        else:
            print(y)
    elif n%3 == 1:
        print(a)
    elif n%3 == 2:
        print(b)
        
    t=t-1

