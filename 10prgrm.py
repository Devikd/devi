b1,b2=input().split(' ')
c=0
for i in range(len(b1)):
    if b1[i]!=b2[i]:
        c=c+1
if(c==1):print('yes')
else:print('no')
