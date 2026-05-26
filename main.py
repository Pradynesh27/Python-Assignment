import json
import math
import os
import glob

def calculate_distance(a, b):
    #Calculates Euclidean distance between two coordinate pairs
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def pkg(name):
    
    target_wh = pkg["warehouse"]

def run_logistics_simulation(input_filepath):
    #Processes a single test JSON file and returns the simulation report dictionary
    with open(input_filepath, 'r') as file:
        data = json.load(file)

    warehouses = data["warehouses"]
    agents_start = data["agents"]
    packages = data["packages"]

    assignments = {agent_id: [] for agent_id in agents_start}
    agent_positions = {agent_id: list(coords) for agent_id, coords in agents_start.items()}

    #  Assign packages to nearest available agent
    for pkg in packages:
        target_wh = (pkg["warehouse"])
        wh_coords = warehouses[target_wh]
        
        best_agent = min(
            agents_start,
            key=lambda a: calculate_distance(agents_start[a], wh_coords)
            )

        assignments[best_agent].append(pkg)
                
        #assignments[best_agent].append(pkg)

    # Simulate deliveries 
    report = {}
    top_agent = None
    lowest_efficiency = float('inf')

    for agent_id in agents_start:
        pkg_queue = assignments[agent_id]
        total_distance = 0.0
        delivered = len(pkg_queue)
        
        for pkg in pkg_queue:
            target_wh = (pkg["warehouse"])
            wh_coords = warehouses[target_wh]
            dest_coords = pkg["destination"]
            
            # Assign packages to nearest available agent
            total_distance += calculate_distance(agent_positions[agent_id], wh_coords)
            total_distance += calculate_distance(wh_coords, dest_coords)
            
            # Update agent's current position state 
            agent_positions[agent_id] = dest_coords
            
        # Compute efficiency [cite: 78]
        efficiency = (total_distance / delivered) if delivered > 0 else 0.0
        
        report[agent_id] = {
            "packages_delivered": delivered,
            "total_distance": round(total_distance, 2),
            "efficiency": round(efficiency, 2)
        }
        
        if delivered > 0 and efficiency < lowest_efficiency:
            lowest_efficiency = efficiency
            top_agent = agent_id

    report["best_agent"] = top_agent
    return report

def process_all_test_cases():
    # Path where test cases are located
    test_folder = "test_cases"
    
    search_pattern = os.path.join(test_folder, "*.json")
    json_files = glob.glob(search_pattern)
    
    if not json_files:
        print(f"No JSON files found in the '{test_folder}' directory. Please create it and add files.")
        return

    print(f"Found {len(json_files)} test case(s). Starting batch processing...\n")

    for file_path in json_files:
        # Extract file name without directory path 
        base_name = os.path.basename(file_path)
        # Create a report name  
        report_folder = "reports"

        if not os.path.exists(report_folder):
            os.makedirs(report_folder)

        output_name = os.path.join(
            report_folder,
            f"report_{base_name}"
        )
        
        print(f"Processing: {base_name} ...")
        try:
            # Run simulation
            results = run_logistics_simulation(file_path)
            
            # Save the report to disk 
            with open(output_name, 'w') as outfile:
                json.dump(results, outfile, indent=4)
            print(f" -> Saved report to: {output_name}")
            
        except Exception as e:
            print(f" -> Failed to process {base_name}. Error: {e}")
            
    print("\nBatch processing completed successfully!")

if __name__ == "__main__":
    process_all_test_cases()