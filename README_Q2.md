Problem 2: Unmanned Ground Vehicle (UGV) Optimal Pathfinding in a Static Grid
1. Problem Statement
An Unmanned Ground Vehicle (UGV) needs to navigate from a user-specified start node to a goal node across a grid map of a small battlefield area (modeled as a 70x70 km space). The environment contains static obstacles known a priori. The density of these obstacles can vary across three different levels (Low, Medium, High). The goal is to design an algorithm that allows the UGV to navigate around known obstacles via the shortest distance while tracking explicit Measures of Effectiveness (MoE).

2. Methodology & Implementation Details
Grid Modeling: The map is represented as a 2D matrix where 0 denotes free traversable space and 1 denotes static obstacles. Obstacles are randomly populated across the grid based on specified probability densities (Low: 10%, Medium: 25%, High: 40%).

Breadth-First Search (BFS): Since all grid traversal step costs are uniform, BFS implemented using a double-ended queue (collections.deque) ensures finding the optimal shortest path in terms of total steps.

Measures of Effectiveness (MoE) Tracking: To evaluate performance across density tiers, the code tracks:

Path Length (Steps): The total number of valid grid movements from start to goal.

Nodes Explored: The total number of unique states/cells expanded during the search process.

Edge Case Handling: The algorithm gracefully handles high-density scenarios where obstacles completely block all valid paths, outputting a clear terminal status notification.

3. Code Structure
create_grid(size, obstacle_density): Dynamically builds the 2D grid matrix and randomizes static obstacle placement while keeping start and goal nodes clear.

bfs_shortest_path(grid, start, goal): Core graph traversal function that evaluates neighboring cells, tracks visited nodes, and returns the navigation path and state exploration count.

Main execution block: Iteratively tests the UGV navigation across Low, Medium, and High obstacle density tiers, outputting formatted terminal reports.

4. Execution & Verification
Run the script from your terminal using:

Bash
python Q2_Static_Grid.py