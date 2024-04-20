def kth_digit(a, b):
    a = abs(a)
    c = a - a % (10**b)
    d = int((c / 10**b) % 10)
    return d
