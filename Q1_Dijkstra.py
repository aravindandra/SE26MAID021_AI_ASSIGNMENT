"""
Question 1: Uniform-Cost Search (Dijkstra's Algorithm) for Indian Cities
Author: Andra Aravind
"""

import heapq

# Graph representing major Indian cities and road distances (in kilometers)
india_road_graph = {
    'Delhi': {'Agra': 233, 'Jaipur': 281, 'Chandigarh': 247},
    'Agra': {'Delhi': 233, 'Lucknow': 335, 'Kanpur': 322},
    'Jaipur': {'Delhi': 281, 'Ahmedabad': 657},
    'Chandigarh': {'Delhi': 247, 'Manali': 310},
    'Lucknow': {'Agra': 335, 'Varanasi': 320},
    'Kanpur': {'Agra': 322, 'Varanasi': 320},
    'Ahmedabad': {'Jaipur': 657, 'Mumbai': 525},
    'Varanasi': {'Lucknow': 320, 'Kanpur': 320, 'Kolkata': 685},
    'Mumbai': {'Ahmedabad': 525, 'Bangalore': 984, 'Hyderabad': 711},
    'Hyderabad': {'Mumbai': 711, 'Bangalore': 569, 'Chennai': 627},
    'Bangalore': {'Mumbai': 984, 'Hyderabad': 569, 'Chennai': 346},
    'Chennai': {'Hyderabad': 627, 'Bangalore': 346, 'Kolkata': 1661},
    'Kolkata': {'Varanasi': 685, 'Chennai': 1661}
}

def uniform_cost_search(graph, start, goal):
    # Priority queue stores tuples of (current_cost, current_node, path_list)
    pq = [(0, start, [start])]
    visited = set()
    
    print(f"--- Running Uniform-Cost Search (Dijkstra) from {start} to {goal} ---")
    
    while pq:
        cost, current, path = heapq.heappop(pq)
        
        if current in visited:
            continue
        visited.add(current)
        
        # If we reached the goal, return the total cost and the path
        if current == goal:
            return cost, path
        
        for neighbor, weight in graph.get(current, {}).items():
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
                
    return float('inf'), []

if __name__ == "__main__":
    start_city = 'Delhi'
    goal_city = 'Bangalore'
    
    total_cost, optimal_path = uniform_cost_search(india_road_graph, start_city, goal_city)
    
    print(f"Optimal Path: {' -> '.join(optimal_path)}")
    print(f"Total Road Distance: {total_cost} km")