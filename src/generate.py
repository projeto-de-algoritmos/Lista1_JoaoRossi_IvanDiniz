import maze
import random

def create_dfs(m):
    stack = []
    current_cell = random.randint(0, m.total_cells - 1)
    visited_cells = 1

    while visited_cells < m.total_cells:
    	unvisited_neighbors = m.cell_neighbors(current_cell)
    	if len(unvisited_neighbors) >= 1:
    		new_cell_index = random.randint(0, len(unvisited_neighbors) - 1)
    		new_cell, compass_index = unvisited_neighbors[new_cell_index]
    		m.connect_cells(current_cell, new_cell, compass_index)
    		stack.append(current_cell)
    		current_cell = new_cell
    		visited_cells +=1
    	else:
    		current_cell = stack.pop()
    	m.refresh_maze_view()
    m.state = "solve"


if __name__ == '__main__':
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    while 1:
        maze.check_for_exit()