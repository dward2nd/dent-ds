def is_overlapped(x1, y1, w1, h1, x2, y2, w2, h2):
    xplane = x2 + w2 < x1 and x2 > x1 + w1  # X plane determination
    yplane = y2 + h2 > y1 and y2 < y1 + h1  # Y plane determination
    return not (xplane and yplane)
