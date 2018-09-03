xx1,yy1=map(int,input().split(' '))
if xx1 > yy1:
    smaller = yy1
else:
    smaller = xx1
for i in range(1, smaller+1):
    if((xx1 % i == 0) and (yy1 % i == 0)):gcd1 = i
print(gcd1)
