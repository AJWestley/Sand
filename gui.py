import pygame as pg
import sand
import uitools
from button import Button
from hourglass import hg

green = (20, 220, 20)
red = (220, 20, 20)


def draw_grid(sandgrid: sand.SandScape, screenheight, screenwidth):
    for y, row in enumerate(sandgrid.grid):
        for x, col in enumerate(row):
            colour = uitools.get_colour(col, sandgrid.can_move)

            x_pos, y_pos = uitools.cell_to_screen(x, y, sandgrid.grid, screenwidth, screenheight)
            cell_size = uitools.get_cell_size(sandgrid.grid, screenheight, screenwidth)
            pg.draw.rect(screen, colour, (x_pos, y_pos, cell_size, cell_size))


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
sand_grid = sand.SandScape(hg)
reset_button = Button(70, 20, 100, 50, "Reset", 5, 30)
pause_button = Button(180, 20, 150, 50, "Pause/Play", 5, 30, text_mult=0.15)
timer = 0
# ------------------------------------ #

# ------------ Debugging ------------- #
'''
for y, row in enumerate(sand_grid.grid):
    for x, cell in enumerate(row):
        print(f'({x}, {y}): {uitools.cell_to_screen(x, y, sand_grid.grid, WIDTH, HEIGHT)} "{cell}"')
'''
# ------------------------------------ #

while running:
    clock.tick(delta)
    timer += 1

    # -------- Event Handling -------- #
    m_x, m_y = pg.mouse.get_pos()

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False
        elif reset_button.check_over(m_x, m_y) and event.type == pg.MOUSEBUTTONDOWN:
            sand_grid.set(hg)
        elif pause_button.check_over(m_x, m_y) and event.type == pg.MOUSEBUTTONDOWN:
            sand_grid.toggle_paused()
    # -------------------------------- #

    # ---------- Rendering ----------- #
    background = pg.Surface(screen.get_size())
    background.fill(uitools.sand_colours['='])
    screen.blit(background, (0, 0))

    draw_grid(sand_grid, HEIGHT, WIDTH)
    reset_button.draw(pg, screen)
    pause_button.draw(pg, screen)

    pg.display.flip()
    # -------------------------------- #

    if timer >= 25:
        sand_grid.update()
        timer = 0
