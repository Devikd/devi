
v = int(input("Enter any number : "))
if v> 1:
    for i in range(2, v):
        if (v % i) == 0:
            print("Yes")
            break
    else:
        print("No")
elif v == 0 or 1:
    print(" a neither prime NOR composite number")
else:
    print("Yes")
