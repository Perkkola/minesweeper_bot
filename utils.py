def index_to_grid(i, width):
    return (i % width, i // width)

def grid_to_index(x, y, width):
    return x + width*y