"""
plots.py
Generates graphs from results.csv
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("../graphs", exist_ok=True)

df = pd.read_csv("../data/results.csv")


def save_plot(x, y, title, ylabel, filename):

    plt.figure(figsize=(10, 5))
    plt.plot(df[x], df[y], linewidth=2)
    plt.title(title)
    plt.xlabel("Simulation Step")
    plt.ylabel(ylabel)
    plt.grid(True)

    plt.savefig(f"../graphs/{filename}", dpi=300)
    plt.close()


# =====================================================
# Professional Flow vs Target Graph
# =====================================================

plt.figure(figsize=(12,6))

plt.plot(
    df["Step"],
    df["Flow"],
    linewidth=3,
    label="Actual Production"
)

plt.plot(
    df["Step"],
    df["TargetFlow"],
    linestyle="--",
    linewidth=2.5,
    label="Target Production"
)

# Highlight the three scenarios
plt.axvspan(
    0,
    24,
    alpha=0.08,
    color="green",
    label="Startup"
)

plt.axvspan(
    25,
    39,
    alpha=0.08,
    color="gold",
    label="Target Change"
)

plt.axvspan(
    40,
    49,
    alpha=0.08,
    color="red",
    label="Infeasible Target"
)

# Vertical markers
plt.axvline(25, color="black", linestyle=":")
plt.axvline(40, color="black", linestyle=":")

# Annotations
plt.annotate(
    "Target Achieved",
    xy=(8,150),
    xytext=(3,170),
    arrowprops=dict(arrowstyle="->")
)

plt.annotate(
    "Target Changed",
    xy=(25,150),
    xytext=(18,205),
    arrowprops=dict(arrowstyle="->")
)

plt.annotate(
    "Maximum Safe Production",
    xy=(45,250),
    xytext=(33,285),
    arrowprops=dict(arrowstyle="->")
)

plt.title(
    "Autonomous Production Choke Controller Performance",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Simulation Step")
plt.ylabel("Oil Production (bbl/hr)")

plt.grid(True)

plt.legend(loc="upper left")

plt.tight_layout()

plt.savefig(
    "../graphs/flow_vs_target.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# Remaining plots
save_plot("Step", "Choke", "Choke Position", "Choke (%)", "choke.png")
save_plot("Step", "WHP", "Wellhead Pressure", "Pressure", "whp.png")
save_plot("Step", "FLP", "Flowline Pressure", "Pressure", "flp.png")
save_plot("Step", "BHP", "Bottomhole Pressure", "Pressure", "bhp.png")

print("Graphs generated successfully!")

import pandas as pd
import matplotlib.pyplot as plt

# Read simulation results
df = pd.read_csv("data/results.csv")   # Change path if needed

plt.figure(figsize=(10,5))

plt.plot(df["Step"], df["TargetFlow"],
         label="Target Oil Rate",
         linewidth=2)

plt.plot(df["Step"], df["Flow"],
         label="Actual Oil Rate",
         linewidth=2)

plt.xlabel("Simulation Step")
plt.ylabel("Oil Rate (bbl/hr)")
plt.title("Target Oil Rate vs Actual Oil Rate")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig("graphs/oil_rate_vs_target.png", dpi=300)
plt.show()