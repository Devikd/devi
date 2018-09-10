initial=int(input())
stair=input().split()
stair=list(map(int,stair))
book=[]
for n in range(1,initial):
  note=0
  for k in range(i):
    if(stair[n]>stair[k]):
      note=note+stair[k]
  book.append(note)
print(sum(book))
