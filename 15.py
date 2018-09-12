ASCII_SIZE = 256
def getMaxOccuringChar(s):
    count = [0] * ASCII_SIZE
    max = -1
    k = ''
    for i in ss:
        count[ord(i)]+=1;
    for i in s:
        if max < count[ord(i)]:
            max = count[ord(i)]
            c = i
    return c
ss =input()
print((getMaxOccuringChar(ss)))
