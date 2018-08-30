def fact(g) :
    if g > 1:
        for i in range(2,g):
            if (v % i) == 0:
                return "no"
        return "yes"
    return "no"
g = int(input(
   "Enter value"))
print(fact(g))
