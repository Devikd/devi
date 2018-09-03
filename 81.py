num=int(input("Enter the number of lines"))
for i in range(num):
    v,g=map(int,input("Ninja's and kabali's value").split(' '))
    print(abs(v-g))
