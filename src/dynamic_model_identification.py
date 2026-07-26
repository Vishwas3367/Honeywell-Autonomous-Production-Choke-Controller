import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("../data/Autonomous_Choke_Control_Simulated_Dataset.csv")

# -----------------------------
# Create Figure
# -----------------------------
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

plots = [
    ("OilRate_bbl_hr", "Oil Rate (bbl/hr)", "Oil Rate vs Choke"),
    ("WHP_psi", "WHP (psi)", "Wellhead Pressure vs Choke"),
    ("FLP_psi", "FLP (psi)", "Flowline Pressure vs Choke"),
    ("BHP_psi", "BHP (psi)", "Bottom Hole Pressure vs Choke"),
]

for ax, (col, ylabel, title) in zip(axes.flat, plots):

    x = df["Choke_pct"]
    y = df[col]

    # Scatter plot
    ax.scatter(
        x,
        y,
        color="royalblue",
        s=35,
        alpha=0.8,
        label="Observed Data"
    )

    # Linear Regression
    m, c = np.polyfit(x, y, 1)

    x_line = np.linspace(x.min(), x.max(), 100)
    y_line = m * x_line + c

    ax.plot(
        x_line,
        y_line,
        color="red",
        linewidth=2,
        label="Regression Line"
    )

    # Equation
    equation = f"y = {m:.3f}x + {c:.3f}"

    ax.text(
        0.05,
        0.92,
        equation,
        transform=ax.transAxes,
        fontsize=10,
        bbox=dict(facecolor="white", alpha=0.8)
    )

    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.set_xlabel("Choke Position (%)")
    ax.set_ylabel(ylabel)
    ax.grid(True)
    ax.legend(fontsize=8)

plt.suptitle(
    "Dynamic Model Identification using Linear Regression",
    fontsize=16,
    fontweight="bold"
)

plt.tight_layout(rect=[0, 0, 1, 0.96])

# -----------------------------
# Save Figure
# -----------------------------
plt.savefig(
    "../graphs/dynamic_model_identification.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nDynamic Model Identification figure saved successfully.")
print("Location: graphs/dynamic_model_identification.png")