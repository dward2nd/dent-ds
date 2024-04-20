def is_leap(n):
    N1 = int(n) // 4
    N2 = int(n) / 4
    A = bool(N1 == N2)
    N3 = int(n) // 100
    N4 = int(n) / 100
    B = bool(N3 == N4)
    N5 = int(n) // 400
    N6 = int(n) / 400
    C = bool(N5 == N6)
    D = (A and (not B)) or C
    return D
