import pandas as pd

# Load simulation results
df = pd.read_csv("../data/results.csv")

# Error calculations
df["Error"] = df["TargetFlow"] - df["Flow"]
df["AbsError"] = df["Error"].abs()

# Performance Metrics
mae = df["AbsError"].mean()
rmse = (df["Error"] ** 2).mean() ** 0.5
max_error = df["AbsError"].max()

# Final steady-state error
steady_state_error = abs(df["Error"].iloc[-1])

# Maximum choke used
max_choke = df["Choke"].max()

# Time (steps) to reach within ±5 bbl/hr of target
tolerance = 5
settling_step = "Not Reached"

for i in range(len(df)):
    if abs(df.loc[i, "Error"]) <= tolerance:
        settling_step = int(df.loc[i, "Step"])
        break

# Pressure Constraint Violations
whp_limit = 350
flp_limit = 250
bhp_limit = 600

whp_violations = (df["WHP"] > whp_limit).sum()
flp_violations = (df["FLP"] > flp_limit).sum()
bhp_violations = (df["BHP"] > bhp_limit).sum()

# Choke Constraint Violations
choke_violations = ((df["Choke"] < 0) | (df["Choke"] > 100)).sum()

print("=" * 60)
print("AUTONOMOUS PRODUCTION CHOKE CONTROLLER")
print("PERFORMANCE METRICS")
print("=" * 60)

print(f"Mean Absolute Error (MAE)      : {mae:.2f} bbl/hr")
print(f"Root Mean Square Error (RMSE)  : {rmse:.2f} bbl/hr")
print(f"Maximum Error                  : {max_error:.2f} bbl/hr")
print(f"Steady-State Error             : {steady_state_error:.2f} bbl/hr")
print(f"Maximum Choke Opening          : {max_choke:.2f} %")
print(f"Settling Step (±5 bbl/hr)      : {settling_step}")

print("\nConstraint Verification")
print("-" * 60)
print(f"WHP Violations                 : {whp_violations}")
print(f"FLP Violations                 : {flp_violations}")
print(f"BHP Violations                 : {bhp_violations}")
print(f"Choke Violations               : {choke_violations}")

print("=" * 60)