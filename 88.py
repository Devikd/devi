xx1,yy1=map(int,input().split(' '))
if xx1 > yy1:
    great = xx1
else:
    great = yy1
while(True):
    if((great % xx1 == 0) and (great % yy1 == 0)):
        lcm = great
        break
    great += 1
print(lcm)
