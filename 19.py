pp=int(input())
ll=list(1 for i in range(pp))
li=[]
for i in range(2,pp,1):
    if l[i]==1:
        for j in range(i*i,pp,i):
            l[j]=0
        if pp%i==0:
            li.append(i)
print(" ".join(str(x) for x in li))
