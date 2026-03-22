import pandas as pd
import numpy as np

# 1. LOAD DATA
# The "weirdly named" doc contains the optimized portfolio structures
xlsm_path = 'dyjtj.xlsm'
details_df = pd.read_excel(xlsm_path, sheet_name='Details')

# Extract allocation for Scenario 1 (Based on the sheet structure observed)
# Rows 7, 8, 9 contain Large, Mid, and Small Cap labels
# Column 21 (Index 21) contains the first set of optimized percentages
portfolio_allocation = {
    'Large Cap': details_df.iloc[7, 21],
    'Mid Cap': details_df.iloc[8, 21],
    'Small Cap': details_df.iloc[9, 21]
}

print(f"Applying Allocation: {portfolio_allocation}")

# 2. SIMULATION SETUP
# We use the Assumptions sheet to understand the risk/return profiles
assumptions = pd.read_csv('Book2.xlsx - Assumptions Sheet.csv')

def run_monte_carlo(allocation, iterations=30):
    success_tracker = []
    
    # Define simplified goal thresholds (Target returns needed to clear debt/inflation)
    # In a full model, this would link to the 'Calc Engine' row-by-row
    goals = ["Health Fund", "Marriage", "Education", "House"]
    
    for i in range(iterations):
        # Simulate annual returns based on asset class volatility
        # Values sourced from Assumptions: Large(14%), Mid(16%), Small(20%)
        l_ret = np.random.normal(0.14, 0.05)
        m_ret = np.random.normal(0.16, 0.08)
        s_ret = np.random.normal(0.20, 0.12)
        
        # Calculate Portfolio Return for this iteration
        total_return = (allocation['Large Cap'] * l_ret + 
                        allocation['Mid Cap'] * m_ret + 
                        allocation['Small Cap'] * s_ret)
        
        # Determine success for each goal based on varying return requirements
        iteration_results = {
            "Health Fund": total_return > 0.06,
            "Marriage": total_return > 0.08,
            "Education": total_return > 0.10,
            "House": total_return > 0.12
        }
        success_tracker.append(iteration_results)

    return pd.DataFrame(success_tracker)

# 3. EXECUTION
sim_df = run_monte_carlo(portfolio_allocation, iterations=30)

# 4. RESULTS CALCULATION
individual_goal_probs = sim_df.mean() * 100
all_goals_met_count = sim_df.all(axis=1).sum()
final_probability = (all_goals_met_count / 30) * 100

print("\n--- Simulation Results (30 Runs) ---")
print(individual_goal_probs.apply(lambda x: f"{x:.1f}% Success Rate"))
print(f"\nFinal Probability all goals are met: {final_probability:.2f}%")