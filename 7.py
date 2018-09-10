v=int(input())
print("0" if v>0 and (v & (v-1))==0 else "1")
