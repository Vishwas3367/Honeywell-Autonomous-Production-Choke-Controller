import pandas as pd
import matplotlib.pyplot as plt
import os

# Read results
df = pd.read_csv("../data/results.csv")

# Output folder
output_dir = "../graphs"
os.makedirs(output_dir, exist_ok=True)

# Scenario names
scenarios = [
    "Startup",
    "Target Change",
    "Infeasible"
]

for scenario in scenarios:

    scenario_df = df[df["Scenario"] == scenario]

    # -----------------------------
    # Target vs Actual Oil Rate
    # -----------------------------
    plt.figure(figsize=(8,4))

    plt.plot(
        scenario_df["Step"],
        scenario_df["TargetFlow"],
        label="Target Oil Rate",
        linewidth=2
    )

    plt.plot(
        scenario_df["Step"],
        scenario_df["Flow"],
        label="Actual Oil Rate",
        linewidth=2
    )

    plt.title(f"{scenario} - Target vs Actual Oil Rate")
    plt.xlabel("Simulation Step")
    plt.ylabel("Oil Rate (bbl/hr)")
    plt.grid(True)
    plt.legend()

    filename = scenario.lower().replace(" ", "_")

    plt.tight_layout()
    plt.savefig(f"{output_dir}/{filename}_target_vs_actual.png", dpi=300)
    plt.close()

    # -----------------------------
    # Choke Position
    # -----------------------------
    plt.figure(figsize=(8,4))

    plt.plot(
        scenario_df["Step"],
        scenario_df["Choke"],
        linewidth=2
    )

    plt.title(f"{scenario} - Choke Position")
    plt.xlabel("Simulation Step")
    plt.ylabel("Choke Position (%)")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(f"{output_dir}/{filename}_choke.png", dpi=300)
    plt.close()

print("Scenario graphs generated successfully!")