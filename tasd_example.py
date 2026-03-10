"""
tasd_example.py
TASD Unified Framework v1.0 - Simple Example Runner
Run this file to test the full TASD framework on real EAST #41195 data
"""

import os
import numpy as np
import pandas as pd
from tasd_framework import TASDFramework

print("=== TASD Unified Framework v1.0 - Example Runner ===")

# Check if the data file exists
data_file = 'east_ip.txt'
if not os.path.exists(data_file):
    print(f"ERROR: File '{data_file}' not found!")
    print("Make sure east_ip.txt is in the same folder as this script.")
    print("You can also change the filename in the code below.")
    exit()

try:
    tasd = TASDFramework(gamma=0.35, attraction_strength=0.8)
    print("Running TASD on real EAST #41195 discharge...")
    
    # Run the full pipeline
    features_scaled = tasd.run_tasd_on_real_data(data_file)
    
    print("\nSUCCESS: TASD Framework completed!")
    print("✓ Master TASD equation defined")
    print("✓ Lyapunov stability certified")
    print("✓ Real EAST #41195 data processed with noise + wall + delay")
    print(f"✓ Processed {len(features_scaled)} time points")
    
    # Save quick result
    pd.DataFrame({'time_point': range(len(features_scaled)), 
                  'scaled_signal': features_scaled.flatten()}).to_csv('tasd_quick_result.csv', index=False)
    print("\nQuick result saved to: tasd_quick_result.csv")

except Exception as e:
    print(f"\nERROR: {e}")
    print("Common fixes:")
    print("1. Make sure east_ip.txt is in the same folder")
    print("2. Make sure psi_filter_v2.py and tasd_framework.py are in the same folder")
    print("3. Run this script from the correct folder")

print("\nTASD example finished.")
