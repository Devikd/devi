v=input("Enter a string")
list1=[]
list2=[]
for i in range(len(v)):
    if i%2==0:list1.append(v[i])
    else:list2.append(v[i])
print("".join(str(x) for x in list1),"".join(str(x) for x in list2))
