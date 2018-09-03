import math
i,j=map(int,input().split(' '))
n1=i*j
if math.sqrt(n1)==int( math.sqrt(n1)):
    print ("Yes")
else:
    print ("No")
