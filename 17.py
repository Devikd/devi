def gcd(aa,ab):
    while ab > 0:
        aa, ab = ab, aa % ab
    return aa
def lcm(aa, ab):
    return aa * ab / gcd(aa, ab)
aa,ab=map(int,input("Enter the values:").split(' '))
print(int(lcm(aa,ab)))
