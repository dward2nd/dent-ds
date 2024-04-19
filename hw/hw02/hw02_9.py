# A function that examine whether 2 rectangles in a coordinate plane is
# overlapped, if it is, it returns true.
def is_overlapped(x1, y1, w1, h1, x2, y2, w2, h2):
    # Calculate the end position of 2 rectangles.
    x1_end = x1 + w1
    x2_end = x2 + w2
    y1_end = y1 + h1
    y2_end = y2 + h2

    # Split the evaluation in halves, x and y
    is_not_overlapped_x = (
        (x1 < x2 and x1_end < x2)
        or (x1 > x2_end and x1_end > x2_end)
        or (x2 < x1 and x2_end < x1)
        or (x2 > x1_end and x2_end > x1_end)
    )
    is_not_overlapped_y = (
        (y1 < y2 and y1_end < y2)
        or (y1 > y2_end and y1_end > y2_end)
        or (y2 < y1 and y2_end < y1)
        or (y2 > y1_end and y2_end > y1_end)
    )

    # Answer the question
    return not (is_not_overlapped_x or is_not_overlapped_y)
