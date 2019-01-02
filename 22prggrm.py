v,kk=raw_input().split()
v=int(v)
kk=int(kk)
l=[]
if v==1 or kk==1:
	print "1"
else:
	for i in range(2,v*kk):
		if (v%i==0 and kk%i==0):
			l.append(i)
	print max(l)
