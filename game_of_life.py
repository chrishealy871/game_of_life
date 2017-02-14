import random
import sys

import pygame

from colours import black, red, black

def draw_grid():
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, black, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, black, (0, y), (width, y))


def draw_cells():
    for (x, y) in cells:
        color = red if cells [x, y] else black
        rectangle = (x * cell_size, y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, color, rectangle)


def get_neighbours((x, y)):
    positions = [(x - 1, y - 1), (x, y + 1), (x + 1, y + 1), (x + 1, y),
                 (x +1,  y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]
    return [cells[c, r] for (c, r) in positions if 0 <= r < rows and 0 <= c < columns]

def evolve():
    global cells

    newCells = cells.copy()

    for position, alive in cells.items():
        live_neighbours = sum(get_neighbours(position))
        if alive:
            if live_neighbours < 2 or live_neighbours > 3:
                newCells[position] = False
        elif live_neighbours == 3:
            newCells[position] = True
    cells = newCells

def get_cells(density=0.2):
    return {(c, r): random.random() < density for c in range(columns) for r in range(rows)}


clock = pygame.time.Clock()

pygame.init()

columns, rows = 100, 100
cells = get_cells()

cell_size = 10
size = width, height = columns * cell_size, rows * cell_size
screen = pygame.display.set_mode(size)


while True:
    clock.tick(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    draw_cells()
    evolve()
    draw_grid()
    pygame.display.update()

