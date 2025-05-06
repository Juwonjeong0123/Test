def rects_collide(rect1, rect2):
    x1, y1, x2, y2 = rect1
    a1, b1, a2, b2 = rect2

    return (
        x1 < a2 and x2 > a1 and
        y1 < b2 and y2 > b1
    )
