import pygame as pg
import sand
import uitools

green = (20, 220, 20)
red = (220, 20, 20)


def draw_grid(sandgrid: sand.SandScape, screenheight, screenwidth):
    for y, row in enumerate(sandgrid.grid):
        for x, col in enumerate(row):
            colour = uitools.get_colour(col, sand_grid.can_move)

            x_pos, y_pos = uitools.cell_to_screen(x, y, sandgrid.grid, screenwidth, screenheight)
            cell_size = uitools.get_cell_size(sandgrid.grid, screenheight, screenwidth)
            pg.draw.rect(screen, colour, (x_pos, y_pos, cell_size, cell_size))


def draw_reset_button():
    button_x, button_y, button_height, button_width = 90, 20, 50, 100
    offset = 5
    outline_colour = uitools.sand_colours['#']
    inside_colour = uitools.sand_colours[' ']
    pg.draw.rect(screen, outline_colour, (button_x, button_y, button_width, button_height))
    pg.draw.rect(screen, inside_colour, (button_x + offset, button_y + offset, button_width - 2*offset, button_height - 2*offset))
    font = pg.font.Font(None, 30)
    text = font.render('Reset', True, uitools.sand_colours['#'])
    screen.blit(text, (button_x + 0.23*button_width, button_y + 0.35*button_height))


# ---------- Initialisation ---------- #
WIDTH, HEIGHT = 400, 600

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))

delta = 100
running = True
clock = pg.time.Clock()
screen.fill((20, 20, 20))
# ------------------------------------ #

# ------------ Variables ------------- #
sand_grid = sand.SandScape(sand.hourglass)
# ------------------------------------ #

# ------------ Debugging ------------- #
'''
for y, row in enumerate(sand_grid.grid):
    for x, cell in enumerate(row):
        print(f'({x}, {y}): {uitools.cell_to_screen(x, y, sand_grid.grid, WIDTH, HEIGHT)} "{cell}"')
'''
# ------------------------------------ #

while running:
    clock.tick(4)

    # -------- Event Handling -------- #
    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False
    # -------------------------------- #

    # ---------- Rendering ----------- #
    background = pg.Surface(screen.get_size())
    background.fill(uitools.sand_colours['='])
    screen.blit(background, (0, 0))

    draw_grid(sand_grid, HEIGHT, WIDTH)
    draw_reset_button()

    pg.display.flip()
    # -------------------------------- #

    # sand_grid.draw_grid()
    sand_grid.update()
