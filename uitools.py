import sand

sand_colours = {
    '0': (225, 191, 146),
    '1': (231, 196, 150),
    '2': (236, 204, 162),
    '3': (242, 210, 169),
    '4': (246, 215, 176),
    '#': (5, 5, 5),
    '=': (228, 250, 255),
    '-': (192, 244, 255),
    ' ': (192, 244, 255),
    'g': (55, 148, 110),
    'r': (172, 50, 50)
}


def screen_to_cell(x, y, grid, screenwidth, screenheight):
    cell_size = get_cell_size(grid, screenheight, screenwidth)
    gridwidth, gridheight = get_grid_size(grid, cell_size)
    h_margin = (screenwidth - gridwidth) // 2
    v_margin = (screenheight - gridheight) // 2

    # check grid bounds
    if (x <= h_margin or x >= gridwidth + h_margin) or (y <= v_margin or y >= gridheight + v_margin):
        return -1, -1

    x -= h_margin
    y -= v_margin

    return x // cell_size, y // cell_size


def cell_to_screen(col, row, grid, screenwidth, screenheight):
    cell_size = get_cell_size(grid, screenheight, screenwidth)
    x = cell_size * col
    y = cell_size * row
    gridwidth, gridheight = get_grid_size(grid, cell_size)
    h_margin = (screenwidth - gridwidth) // 2
    v_margin = (screenheight - gridheight) // 2
    x += h_margin
    y += v_margin
    y = screenheight - y
    return x, y


def get_cell_size(grid, screenheight, screenwidth):
    # 5% screen size margin on either side
    effective_height = 0.8 * screenheight
    effective_width = 0.8 * screenwidth

    cell_height = effective_height // len(grid)
    cell_width = effective_width // len(grid[0])

    # cells must be square
    return min(cell_height, cell_width)


def get_grid_size(grid, cell_size):
    return len(grid[0]) * cell_size, len(grid) * cell_size


def get_colour(cell_value, can_move: bool):
    if cell_value == '!':
        if can_move:
            return sand_colours['g']
        else:
            return sand_colours['r']
    else:
        return sand_colours[cell_value]
