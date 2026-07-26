import csv
import os

import config
from controller import AutonomousController
from simulator_stub import OilWellSimulator

simulator = OilWellSimulator()
controller = AutonomousController()

history = []

print("=" * 65)
print("Honeywell Autonomous Production Choke Controller")
print("=" * 65)

for step in range(50):

    # -------- Scenario Selection --------
    if step < config.TARGET_CHANGE_STEP:
        target = config.INITIAL_TARGET_FLOW
        scenario = "Startup"

    elif step < 40:
        target = config.NEW_TARGET_FLOW
        scenario = "Target Change"

    else:
        target = config.INFEASIBLE_TARGET_FLOW
        scenario = "Infeasible"

    measurements = simulator.step(controller.current_choke)

    new_choke = controller.control(measurements, target)

    row = {
        "Step": step,
        "Scenario": scenario,
        "TargetFlow": target,
        "Flow": measurements["flow"],
        "WHP": measurements["whp"],
        "FLP": measurements["flp"],
        "BHP": measurements["bhp"],
        "Choke": new_choke
    }

    history.append(row)

    print(
        f"{scenario:12} | "
        f"Step {step:02d} | "
        f"Target={target:.0f} | "
        f"Flow={measurements['flow']:.2f} | "
        f"Choke={new_choke:.1f}%"
    )

os.makedirs("../data", exist_ok=True)

with open("../data/results.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=history[0].keys())
    writer.writeheader()
    writer.writerows(history)

print("\nSimulation completed.")
print("Results saved to data/results.csv")