def stylo(mm):
  x=0
  for i in range(len(mm)):
    for j in range(i+1,len(mm)):
      if(mm[i]==mm[j]):
        return 0
  return(len(mm))
w=input()
x=[]
for i in range(len(w)):
  for j in range(i+1,len(w)+1):
    x.append(stylo(w[i:j]))
print(max(x))
