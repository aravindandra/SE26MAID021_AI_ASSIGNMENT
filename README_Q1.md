# Problem 1: Uniform-Cost Search (Dijkstra's Algorithm) for Indian Road Networks

## 1. Problem Statement
When actions have different costs in a state-based search space, an optimal strategy is to use Best-First Search where the evaluation function evaluates the path cost from the root node to the current node. In the theoretical computer science community, this is known as **Dijkstra's Algorithm**, while the AI community refers to it as **Uniform-Cost Search (UCS)**. The objective of this problem is to implement Dijkstra's algorithm to compute the shortest road distances between major cities in India.

---

## 2. Methodology & Implementation Details
* **Graph Representation:** The road network is modeled as a weighted undirected graph using a Python dictionary (`india_road_graph`), where keys represent cities and values represent neighboring connected cities with corresponding road distances in kilometers.
* **Priority Queue (`heapq`):** To efficiently extract the node with the lowest cumulative path cost, Python's built-in binary heap implementation (`heapq`) is utilized. 
* **State Tracking:** A `visited` set is maintained to keep track of expanded nodes, ensuring that each city is processed only once at its optimal (minimum) cost.
* **Path Reconstruction:** Each state in the priority queue stores a tuple containing `(current_cumulative_cost, current_node, path_history)`, allowing the script to return both the exact optimal path and the total distance.

---

## 3. Code Structure
* `india_road_graph`: Dictionary mapping major cities (e.g., Delhi, Mumbai, Bangalore, Jaipur) to their immediate neighbors and edge weights.
* `uniform_cost_search(graph, start, goal)`: Core function implementing the priority queue expansion logic.
* Main execution block: Configures the start city ('Delhi') and goal city ('Bangalore'), invokes the search function, and formats the output.

---

## 4. Execution & Verification
Run the script from your terminal using:
```bash
python Q1_Dijkstra.py