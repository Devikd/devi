vv=input("enter the string")
gg=''
ch=''
for i in range(len(vv)):
    gg+=str(ord(vv[i])+3)
print(gg)
for i in range(len(gg)):
    ch+=chr(int(gg[i]))
print(ch)
