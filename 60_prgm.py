g=int(input("Enter Fibonacci Range"))
g1 = 0
g2 = 1
count = 0
l=[]
if g == 1:
    l.append(g1)
else:
    while count < g:
        l.append(g1)
        gth = g1 + g2
        g1 = g2
        g2 = nth
        count += 1
print(" ".join(str(x) for x in l))
