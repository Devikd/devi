def is_perfect_square(n):
    m= n // 2
    s= set([x])
    while m * m != n:
        m = (m + (s // n)) // 2
        if m in s: return False
        y.add(m)
    return True

print(is_perfect_square(8))
print(is_perfect_square(9))
print(is_perfect_square(100))
