vl=list(input())
for i in range(0,len(vl)-1,2):
    vl[i],l[i+1]=l[i+1],l[i]
print("".join(str(x) for x in vl))
