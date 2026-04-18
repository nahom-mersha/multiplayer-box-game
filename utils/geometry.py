def get_width_height(item):
    x1, y1, x2, y2 = item
    return (x2-x1,y2-y1)

def get_center(item):
    x1, y1, x2, y2 = item
    return ((x2-x1)/2,(y2-y1)/2)

def get_four_quadrant_centers(item):
    x1, y1, x2, y2 = item
    horizontal_shift, vertical_shift = ((x2-x1)/2,(y2-y1)/2)
    quadrant_1 = (horizontal_shift + horizontal_shift/2 , vertical_shift - vertical_shift/2)
    quadrant_2 = (horizontal_shift - horizontal_shift/2 , vertical_shift - vertical_shift/2)
    quadrant_3 = (horizontal_shift - horizontal_shift/2 , vertical_shift + vertical_shift/2)
    quadrant_4 = (horizontal_shift + horizontal_shift/2 , vertical_shift + vertical_shift/2)
    return (quadrant_1, quadrant_2, quadrant_3, quadrant_4)
def get_canvas_height_width(canvas):
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    return (width, height)
