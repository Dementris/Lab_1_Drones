import pygame
from dsa_graphics import init_pygame, draw_grid, observer, FPS
from dsa_automaton import init_grid, update_grid, GRID_W, GRID_H


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
    run_simulation()