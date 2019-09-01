import maze
import generate
import sys
import random
import pygame


def bfs_solver(m):
    queue = []
    cur_cell = 0
    in_direction = 0b0000
    visited_cells = 0
    queue.insert(0, (cur_cell, in_direction))
    while not cur_cell == len(m.maze_array) - 1 and len(queue) > 0:
        cur_cell, in_direction = queue.pop()
        m.bfs_visit_cell(cur_cell, in_direction)
        visited_cells += 1
        m.refresh_maze_view()
        neighbors = m.cell_neighbors(cur_cell)
        for neighbor in neighbors:
            queue.insert(0, neighbor)
    m.reconstruct_solution(cur_cell)
    m.state = "idle"

def print_solution_array(m):
    solution = m.solution_array()
    print('Solution ({} steps): {}'.format(len(solution), solution))

if __name__ == '__main__':
    current_maze = maze.Maze('create')
    generate.create_dfs(current_maze)
    
    bfs_solver(current_maze)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        




