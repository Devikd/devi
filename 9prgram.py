low,upp=map(int,input().split(' '))
ll=list(1 for i in range(upp+1))
b=0
for i in range(2,upp+1,1):
    if ll[i]==1:
        for j in range(i*i,upp+1,i):
            ll[j]=0
        if i>=low:
             b+=1
print(b)
