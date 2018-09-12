kk=raw_input()
vv=a[::-1]
if kk==vv:
	print "0"
else:
	s=0
	l=[]
	for i in range(0,len(kk)):
		l.append(kk[i])
	res=[]
	for i in l:
		if l.count(i)==1:
			res.append(i)
	print len(res)
