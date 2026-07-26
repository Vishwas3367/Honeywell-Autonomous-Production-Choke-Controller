# Autonomous Production Choke Controller

## Honeywell Hackathon 2026

An autonomous production choke controller developed for the Honeywell Hackathon to automatically regulate oil production while maintaining safe operating conditions. The controller uses process prediction, optimization, and safety constraint handling to determine the optimal choke position for different operating scenarios.

---

# Problem Statement

Develop an autonomous choke controller for a naturally flowing oil well that:

- Achieves the desired oil production target.
- Maintains safe operating pressures.
- Handles startup conditions.
- Responds to production target changes.
- Safely manages infeasible production targets.

---

# Objectives

- Perform open-loop step-test analysis.
- Develop a dynamic process model from the provided dataset.
- Design an autonomous choke controller.
- Maintain safe WHP, FLP, and BHP limits.
- Optimize choke movements.
- Evaluate controller performance using simulation.

---

# Project Structure

```
Honeywell_Choke_Controller/
│
├── data/
│   ├── Autonomous_Choke_Control_Simulated_Dataset.csv
│   └── results.csv
│
├── graphs/
│   ├── flow_vs_target.png
│   ├── choke.png
│   ├── whp.png
│   ├── flp.png
│   ├── bhp.png
│   ├── step_oilrate.png
│   ├── step_whp.png
│   ├── step_flp.png
│   ├── step_bhp.png
│   └── dynamic_model_identification.png
│
├── report/
│
├── presentation/
│
├── src/
│   ├── config.py
│   ├── constraints.py
│   ├── controller.py
│   ├── optimizer.py
│   ├── simulator_stub.py
│   ├── metrics.py
│   ├── plots.py
│   ├── step_test_analysis.py
│   ├── dynamic_model_identification.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

# Methodology

The project follows the workflow below:

```
Dataset
      ↓
Open-loop Step Test
      ↓
Dynamic Model Identification
      ↓
Controller Design
      ↓
Constraint Checking
      ↓
Predictive Choke Optimization
      ↓
Closed-loop Simulation
      ↓
Performance Evaluation
```

---

# Dynamic Model Identification

The process model was obtained using linear regression on the supplied dataset.

Oil Rate

```
Oil Rate = 1.642 × Choke + 44.679
```

Wellhead Pressure (WHP)

```
WHP = -1.101 × Choke + 298.038
```

Flowline Pressure (FLP)

```
FLP = -0.777 × Choke + 210.475
```

Bottom Hole Pressure (BHP)

```
BHP = -4.431 × Choke + 3236.276
```

---

# Control Strategy

The autonomous controller performs the following operations:

- Predicts oil production for multiple choke positions.
- Estimates pressure responses.
- Checks operational constraints.
- Optimizes choke movement.
- Applies the safest and most effective choke setting.

Optimization objective:

```
Cost = Tracking Error + Movement Penalty
```

---

# Simulation Scenarios

### Scenario A – Startup

- Target Production: **150 bbl/hr**
- Controller reaches the desired production smoothly.

### Scenario B – Target Change

- Target Production: **180 bbl/hr**
- Controller automatically adjusts choke position.

### Scenario C – Infeasible Target

- Target Production: **300 bbl/hr**
- Controller settles at the maximum achievable safe production.

---

# Performance Metrics

| Metric | Value |
|---------|--------|
| Mean Absolute Error (MAE) | 24.28 bbl/hr |
| Root Mean Square Error (RMSE) | 41.17 bbl/hr |
| Maximum Tracking Error | 125.34 bbl/hr |
| Steady-State Error | 52.75 bbl/hr |
| Constraint Violations | 0 |

---

# Generated Results

The project generates the following plots:

- Oil Production vs Target
- Choke Position
- Wellhead Pressure (WHP)
- Flowline Pressure (FLP)
- Bottom Hole Pressure (BHP)
- Step-Test Analysis
- Dynamic Model Identification

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

Run the controller

```bash
cd src
python main.py
```

Generate step-test analysis

```bash
python step_test_analysis.py
```

Generate dynamic model identification

```bash
python dynamic_model_identification.py
```

Compute performance metrics

```bash
python metrics.py
```

---

# Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib

---

# Future Improvements

- Model Predictive Control (MPC)
- Machine Learning-based process prediction
- Real-time sensor integration
- SCADA system connectivity
- Multi-well optimization

---

# Authors

**Honeywell Hackathon Team**

- Vishwas Kumar
- (Team Member Name)

---

# Acknowledgements

This project was developed as part of the Honeywell Hackathon using the provided Autonomous Choke Control simulated dataset and simulator.