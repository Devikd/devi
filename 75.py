vt=input()
if(len(vt)%2==0):
    vt=vt[:int((len(vt)/2))-1]+'**'+vt[int(len(vt)/2)+1:]
else:
    vt=vt[:int(len(vt)/2)]+'*'+vt[int(len(vt)/2)+1:]
print(vt)
