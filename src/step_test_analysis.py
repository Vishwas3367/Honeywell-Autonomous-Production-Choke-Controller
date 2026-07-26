import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/Autonomous_Choke_Control_Simulated_Dataset.csv")
print(df.columns)
print(df.head())

print("\n===== STEP TEST SUMMARY =====")
print(df.describe())

# Oil Rate
plt.figure(figsize=(10,5))
plt.plot(df["Time_hr"], df["OilRate_bbl_hr"], linewidth=2)
plt.title("Open Loop Step Test - Oil Rate")
plt.xlabel("Time (hr)")
plt.ylabel("Oil Rate (bbl/hr)")
plt.grid(True)
plt.savefig("../graphs/step_oilrate.png")
plt.close()

# WHP
plt.figure(figsize=(10,5))
plt.plot(df["Time_hr"], df["WHP_psi"], linewidth=2)
plt.title("Open Loop Step Test - Wellhead Pressure")
plt.xlabel("Time (hr)")
plt.ylabel("WHP (psi)")
plt.grid(True)
plt.savefig("../graphs/step_whp.png")
plt.close()

# FLP
plt.figure(figsize=(10,5))
plt.plot(df["Time_hr"], df["FLP_psi"], linewidth=2)
plt.title("Open Loop Step Test - Flowline Pressure")
plt.xlabel("Time (hr)")
plt.ylabel("FLP (psi)")
plt.grid(True)
plt.savefig("../graphs/step_flp.png")
plt.close()

# BHP
plt.figure(figsize=(10,5))
plt.plot(df["Time_hr"], df["BHP_psi"], linewidth=2)
plt.title("Open Loop Step Test - Bottom Hole Pressure")
plt.xlabel("Time (hr)")
plt.ylabel("BHP (psi)")
plt.grid(True)
plt.savefig("../graphs/step_bhp.png")
plt.close()

print("\nStep-test plots generated successfully.")
import numpy as np

print("\n===== DYNAMIC MODEL IDENTIFICATION =====")

flow_coeff = np.polyfit(df["Choke_pct"], df["OilRate_bbl_hr"], 1)
whp_coeff = np.polyfit(df["Choke_pct"], df["WHP_psi"], 1)
flp_coeff = np.polyfit(df["Choke_pct"], df["FLP_psi"], 1)
bhp_coeff = np.polyfit(df["Choke_pct"], df["BHP_psi"], 1)

print(f"Oil Rate ≈ {flow_coeff[0]:.3f} × Choke + {flow_coeff[1]:.3f}")
print(f"WHP      ≈ {whp_coeff[0]:.3f} × Choke + {whp_coeff[1]:.3f}")
print(f"FLP      ≈ {flp_coeff[0]:.3f} × Choke + {flp_coeff[1]:.3f}")
print(f"BHP      ≈ {bhp_coeff[0]:.3f} × Choke + {bhp_coeff[1]:.3f}")