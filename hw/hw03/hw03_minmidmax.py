def min_mid_max(a: float, b: float, c: float) -> float:
    # assume that initially min := a, mid := b, max := c
    # I use mn as min, mx as max to avoid conflict with actual Python functions
    # called min() and max()

    # First, find min and max out of a, b, c
    mn, md, mx = a, b, c
    if mn > mx:
        mn, mx = mx, mn  # switching the value
    # if mn > mx is False, no action is needed.

    # Then insert md and find which one gets to be middle,
    # become min or become max
    if md > mx:
        mx, md = md, mx
    elif md < mn:
        mn, md = md, mn

    # now mn, md, mx are sorted
    return mn, md, mx


if __name__ == "__main__":
    a, b, c = [int(x) for x in input().split()]
    print(min_mid_max(a, b, c))
