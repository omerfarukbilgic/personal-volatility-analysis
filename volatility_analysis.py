"""
Project: Personal Volatility & Utility Analysis (2025 Simulation)
Author: Omer Faruk
Description: A data analysis simulation testing the hypothesis that high-volatility days (Crises),
despite their negative nature, yield higher long-term utility compared to low-performance days.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. SETUP: Create Date Range for the Year
dates = pd.date_range(start='2025-01-01', end='2025-12-31', freq='D')
df = pd.DataFrame(dates, columns=['Date'])

# 2. SIMULATION: Assign Categories based on Probability
# Categories:
# - Stable: Routine days (Low Risk / Avg Reward)
# - Peak: High performance days (Good days)
# - Low_Perf: Unproductive/Bad days (Low Utility)
# - Crisis: High volatility events (High Risk / High Learning Opportunity)

categories = ['Stable', 'Peak', 'Low_Perf', 'Crisis']
probabilities = [0.50, 0.20, 0.20, 0.10] # 50% Stable, 10% Crisis etc.

# Randomly assign categories to days
np.random.seed(42) # Fixed seed for reproducibility
df['Category'] = np.random.choice(categories, size=len(df), p=probabilities)

# 3. UTILITY SCORING ALGORITHM (The Hypothesis)
def calculate_utility(row):
    category = row['Category']
    
    if category == 'Stable':
        # Routine days yield average utility (Safe zone), unspecified dates are usually within this range
        return np.random.randint(1, 4) # Returns 1, 2, or 3
    
    elif category == 'Peak':
        # Peak days are highly productive
        return np.random.randint(3, 6) # Returns 3, 4, or 5
    
    elif category == 'Low_Perf':
        # "Bad" days are mostly waste of time (Low Utility)
        return np.random.randint(0, 3) # Returns 0, 1, or 2
    
    elif category == 'Crisis':
        # "Crisis" days are volatile: Either hitting rock bottom (0-1) 
        # or providing massive life lessons (4-5).
        # Hypothesis: Higher variance than 'Stable' days.
        return np.random.choice([0, 1, 4, 5], p=[0.3, 0.2, 0.2, 0.3])

# Apply the function
df['Utility_Score'] = df.apply(calculate_utility, axis=1)

# ---------------------------------------------------------
# 4. DATA OVERRIDE (MANUAL ENTRY)
# Real-world data entry for specific remembered dates.
# This overrides the simulation for accuracy.
# ---------------------------------------------------------

actual_events = [
    # Format: ('YYYY-MM-DD', 'Category', Score)
    ('2025-01-01', 'Peak', 3), 
    ('2025-01-09', 'Crisis', 1),  
    ('2025-01-10', 'Peak', 3),   
    ('2025-01-11', 'Low_Perf', 1),
    ('2025-01-13', 'Low_Perf', 1),
    ('2025-01-14', 'Low_Perf', 1),
    ('2025-01-16', 'Low_Perf', 1),
    ('2025-01-18', 'Crisis', 1),
    ('2025-01-19', 'Crisis', 1),
    ('2025-01-20', 'Crisis', 1),
    ('2025-01-21', 'Crisis', 1),
    ('2025-01-22', 'Low_Perf', 1),
    ('2025-01-27', 'Peak', 3),
    ('2025-01-28', 'Peak', 5),
    ('2025-01-30', 'Crisis', 1),
    ('2025-02-26', 'Crisis', 1),
    ('2025-03-01', 'Peak', 5),
    ('2025-03-08', 'Peak', 5),
    ('2025-03-11', 'Peak', 1),
    ('2025-03-12', 'Crisis', 5),
    ('2025-03-19', 'Crisis', 1),
    ('2025-03-22', 'Crisis', 5),
    ('2025-05-31', 'Peak', 5),
    ('2025-06-01', 'Peak', 5),
    ('2025-06-01', 'Peak', 5),
    ('2025-06-25', 'Crisis', 5),
    ('2025-07-01', 'Crisis', 4),
    ('2025-07-02', 'Peak', 3),
    ('2025-07-04', 'Crisis', 5),
    ('2025-07-16', 'Low_Perf', 2),
    ('2025-07-17', 'Low_Perf', 2),
    ('2025-07-18', 'Peak', 3),
    ('2025-07-19', 'Crisis', 1),
    ('2025-07-20', 'Low_Perf', 4),
    ('2025-07-21', 'Crisis', 5),
    ('2025-08-14', 'Peak', 3),
    ('2025-08-15', 'Peak', 3),
    ('2025-08-28', 'Crisis', 5),
    ('2025-09-20', 'Peak', 3),
    ('2025-09-21', 'Peak', 3),
    ('2025-10-06', 'Peak', 5),
    ('2025-10-14', 'Peak', 5),
    ('2025-10-17', 'Crisis', 1),
    ('2025-10-24', 'Peak', 5),
    ('2025-11-19', 'Crisis', 1),
    ('2025-11-20', 'Crisis', 5),
    ('2025-11-24', 'Low_Perf', 1),
    ('2025-11-25', 'Low_Perf', 1),
    ('2025-11-26', 'Low_Perf', 2),
    ('2025-11-27', 'Peak', 5),
    ('2025-12-01', 'Peak', 4)
]

for date, cat, score in actual_events:
    mask = df['Date'] == date
    df.loc[mask, 'Category'] = cat
    df.loc[mask, 'Utility_Score'] = score

# ---------------------------------------------------------

# 5. ANALYSIS & VISUALIZATION 📊

print("\n--- ANNUAL UTILITY SUMMARY ---")
summary = df.groupby('Category')['Utility_Score'].describe()
print(summary[['count', 'mean', 'std']])

# Visualization: Boxplot to show Volatility (Variance)
plt.figure(figsize=(12, 7))

# Define custom colors for professional look
custom_palette = {
    'Stable': '#A8D0E6',    # Light Blue
    'Peak': '#374785',      # Dark Blue
    'Low_Perf': '#F76C6C',  # Light Red
    'Crisis': '#24305E'     # Navy/Dark (Intense)
}

sns.boxplot(
    x='Category', 
    y='Utility_Score', 
    hue='Category',  
    data=df, 
    order=['Stable', 'Peak', 'Low_Perf', 'Crisis'], 
    palette=custom_palette,
    legend=False   
)

plt.title('Volatility Analysis: Impact of High-Variance Events on Utility', fontsize=14, fontweight='bold')
plt.ylabel('Utility Score (0-5)', fontsize=12)
plt.xlabel('Daily Category', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.4)

plt.show()

# 6. EXPORT
df.to_csv('utility_analysis_2025.csv', index=False)
print("\n✅ Analysis complete. Data exported to 'utility_analysis_2025.csv'.")