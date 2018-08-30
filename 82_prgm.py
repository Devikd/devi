ee=['a','e','i','o','u','A','E','I','O','U']
def vw(s):
    for i in ee:
        if i in s:
            return "yes"
    return "no"
s=list(input("Enter the string"))
print(eew(s))
