import pygame
from dsa_graphics import init_pygame, draw_grid, observer, FPS
from dsa_automaton import init_grid, update_grid, GRID_W, GRID_H
import numpy as np
import matplotlib.pyplot as plt

QUITE_80 =  pygame.event.custom_type()

def show_plot(visited_share_array):
    growth = np.diff(visited_share_array)
    iterations =  np.arange(1, len(visited_share_array))
    plt.figure(figsize=(10, 6))
    plt.plot(iterations, growth, color='red')
    plt.title('Графік приросту прогресу від однієї ітерації до іншої')
    plt.xlabel('iteration')
    plt.ylabel('%')
    plt.grid()
    plt.show()

def eighty_percent_interruption(visited_share):
    if visited_share >= 0.8:
        QUITE_80_event = pygame.event.Event(QUITE_80)
        pygame.event.post(QUITE_80_event)

def run_eighty_percent_simulation():
    grid = init_grid()
    screen = init_pygame(GRID_W, GRID_H)
    draw_result = draw_grid(screen, grid)
    if draw_result is None:
        return
    clock = pygame.time.Clock()

    running = True
    iter_count = 0

    visited_share_array = []
    while running:
        for event in pygame.event.get():
            if event.type == QUITE_80:
                running = False
        # Update simulation
        new_grid = update_grid(grid, iter_count)
        if new_grid is None:
            break
        # Gather plot data
        visited_share = observer(new_grid, grid, iter_count)
        eighty_percent_interruption(visited_share)
        visited_share_array.append(visited_share*100)

        # Draw everything
        draw_result = draw_grid(screen, new_grid, grid)
        if draw_result is None:
            break

        grid = new_grid
        clock.tick(FPS)
        iter_count += 1

    pygame.quit()
    show_plot(visited_share_array)
    print('Simulation terminated.')


# Main loop
def run_simulation():
    grid = init_grid()
    screen = init_pygame(GRID_W, GRID_H)
    draw_result = draw_grid(screen, grid)
    if draw_result is None:
        return
    clock = pygame.time.Clock()
    running = True
    iter_count = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update simulation
        new_grid = update_grid(grid, iter_count)
        if new_grid is None:
            break
        observer(new_grid, grid, iter_count)

        # Draw everything
        draw_result = draw_grid(screen, new_grid, grid)
        if draw_result is None:
            break        
        
        grid = new_grid
        clock.tick(FPS)
        iter_count += 1
    
    pygame.quit()
    print('Simulation terminated.')


if __name__ == '__main__':
    run_eighty_percent_simulation()