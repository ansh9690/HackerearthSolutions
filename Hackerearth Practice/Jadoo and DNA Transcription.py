b=input()
a="GCTA";c="CGAU"
try:print(''.join([c[a.index(i)]for i in b]))
except:print("Invalid Input")