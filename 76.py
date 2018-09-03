vt=int(input())
fact=0
for i in range(1,vt):
  if vt%i==0:
    fact=i
if fact>1:
  print ('Yes')
elif vt==1:
  print ('neither prime nor composite')
else:
  print ('No')
