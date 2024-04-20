def t(s):
    ss = s % 60
    m = s // 60
    m2 = m % 60
    h = s // 3600
    return f"{h:02d}:{m2:02d}:{ss:02d}"
