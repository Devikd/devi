vx=int(input())
lx=[]
for i in range(1, vx + 1):
       if vx % i == 0:
           lx.append(i)
print(" ".join(str(n) for n in lx))
