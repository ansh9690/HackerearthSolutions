s = input()

newstring = "" 

for a in s: 
	if (a.isupper()) == True:
		newstring+=(a.lower()) 
 
	elif (a.islower()) == True: 
		newstring+=(a.upper()) 
 
	elif (a.isspace()) == True: 
		newstring+= a 

print(newstring) 
