Problem 3: UGV Navigation in a Dynamic Obstacles Environment
1. Problem Statement
In real-world operational environments, the assumption of static obstacles breaks down. Obstacles can be dynamic, unpredictable, and unknown a priori. This problem relaxes the static environment condition from Question 2, requiring a robust runtime strategy for the UGV to navigate, perceive unexpected changes in real-time, and execute dynamic re-routing to successfully reach the goal.

2. Methodology & Implementation Details
Iterative Re-planning Framework: Instead of computing a single rigid global path upfront, the UGV executes an incremental step-by-step navigation loop, evaluating its directional progress toward the goal at each tick.

Dynamic Obstacle Simulation: A probabilistic event handler introduces unexpected obstacles mid-execution (with a 15% random chance per movement step) to simulate runtime environment changes.

Real-Time Obstacle Avoidance: When a dynamic obstacle suddenly occupies the intended next coordinate position, the UGV intercepts the blockage locally and dynamically shifts to an alternative safe lateral coordinate before resuming its route.

Trajectory Logging: The framework records total runtime steps and final trajectory length to measure execution efficiency under disruption.

3. Code Structure
simulate_dynamic_navigation(): Manages the step-by-step movement loop, coordinate tracking, and target validation logic.

Dynamic interruption block: Simulates real-time sensor detection of unexpected obstacles and triggers immediate path adjustments.

Main execution block: Initializes the simulation environment and logs step-by-step traversal updates to the console.

4. Execution & Verification
Run the script from your terminal using:

Bash
python Q3_UGV_Navigation.py