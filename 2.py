a,b=raw_input().split()
b=int(b)
c=len(a)
d=[]
for i in range(0,c):
	s=a[i]
	d.append(s)
w=c-b
v=[]
for i in range(b,c):
	s=d[i]
	v.append(s)
print "".join(v)
	
