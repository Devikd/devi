l1,l2,k=input().split(' ')
kd=int(kd)
s=0
for i in range(len(l1)):
    if l1[i]!=l2[i]:
        s+=1
if s==kd:print("yes")
else:print("no")
