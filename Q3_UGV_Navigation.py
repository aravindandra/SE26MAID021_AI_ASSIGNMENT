"""
Question 3: UGV Navigation with Dynamic Obstacles
Author: Andra Aravind
"""

import random

def simulate_dynamic_navigation():
    print("--- Initializing Dynamic Environment Simulation for UGV ---")
    grid_size = 20
    start = (0, 0)
    goal = (grid_size - 1, grid_size - 1)
    
    current_pos = start
    path_taken = [current_pos]
    steps = 0
    max_steps = 100
    
    while current_pos != goal and steps < max_steps:
        steps += 1
        r, c = current_pos
        gr, gc = goal
        
        # Move one step closer to goal heuristically
        dr = 1 if gr > r else (-1 if gr < r else 0)
        dc = 1 if gc > c else (-1 if gc < c else 0)
        
        next_pos = (r + dr, c + dc)
        
        # Simulate dynamic obstacle appearance randomly with 15% probability
        if random.random() < 0.15 and next_pos != goal:
            print(f"Step {steps}: Dynamic obstacle detected at {next_pos}! Re-routing...")
            # Take an alternate safe step (e.g., move laterally)
            next_pos = (r, c + 1) if c + 1 < grid_size else (r + 1, c)
            
        current_pos = next_pos
        path_taken.append(current_pos)
        
        if current_pos == goal:
            print(f"Success! UGV reached the goal at {goal} in {steps} dynamic steps.")
            break
            
    print(f"Total dynamic path trajectory length: {len(path_taken)}")

if __name__ == "__main__":
    simulate_dynamic_navigation()