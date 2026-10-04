"""
Question 2: UGV Optimal Pathfinding in a Static Grid Environment
Author: Andra Aravind
"""

import random
from collections import deque

def create_grid(size=70, obstacle_density=0.2):
    # 0 = Free cell, 1 = Obstacle
    grid = [[0 for _ in range(size)] for _ in range(size)]
    num_obstacles = int(size * size * obstacle_density)
    
    count = 0
    while count < num_obstacles:
        r = random.randint(0, size - 1)
        c = random.randint(0, size - 1)
        if (r, c) != (0, 0) and (r, c) != (size - 1, size - 1) and grid[r][c] == 0:
            grid[r][c] = 1
            count += 1
    return grid

def bfs_shortest_path(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    queue = deque([[start]])
    visited = {start}
    nodes_visited = 0
    
    while queue:
        path = queue.popleft()
        r, c = path[-1]
        nodes_visited += 1
        
        if (r, c) == goal:
            return path, nodes_visited
            
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(path + [(nr, nc)])
                
    return None, nodes_visited

if __name__ == "__main__":
    grid_size = 35 # Scaled for reasonable terminal output execution, represents area model
    start_node = (0, 0)
    goal_node = (grid_size - 1, grid_size - 1)
    
    # Test three different levels of obstacle density
    densities = {"Low": 0.1, "Medium": 0.25, "High": 0.4}
    
    for level, density in densities.items():
        print(f"\n--- Testing UGV Navigation with {level} Density ({density*100}%) ---")
        grid = create_grid(grid_size, density)
        path, nodes_explored = bfs_shortest_path(grid, start_node, goal_node)
        
        if path:
            print(f"Status: Path Found!")
            print(f"Path Length (Steps): {len(path)}")
            print(f"Measures of Effectiveness (MoE) - Nodes Explored: {nodes_explored}")
        else:
            print(f"Status: No path found. Blocked by obstacles.")