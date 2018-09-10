aax=int(input("enter aa-x"))
aay=int(input("enter aa-y"))
bbx=int(input("enter bb-x"))
bby=int(input("enter bb-y"))
ccx=int(input("enter cc-x"))
ccy=int(input("enter cc-y"))
ddx=int(input("enter dd-x"))
ddy=int(input("enter dd-y"))
if aax==aay and aay==bbx and bby==ccx and ccx==ccy and ccy==ddx and ddy==aax:
    print("yes")
else:
    print("no")
