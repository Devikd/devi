
x=raw_input("X :")
y=raw_input("y :")
v=abs(len(x)-len(y))
n=len(min(x,y))
x=list(x)
y=list(y)
for i in xrange(n):
    if x[i]!=y[i]:
        v+=1
print v
