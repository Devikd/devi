l=list(input())
k1=[]
for v1 in l:
    if v1.isdigit():
        k1.append(v1)
print("".join(str(n) for n in k1))
