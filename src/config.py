"""
config.py
Configuration parameters for the Autonomous Production Choke Controller
"""

# -----------------------------
# Production Targets
# -----------------------------

INITIAL_TARGET_FLOW = 150.0
TARGET_CHANGE_STEP = 25
NEW_TARGET_FLOW = 180.0
INFEASIBLE_TARGET_FLOW = 300.0

# -----------------------------
# Choke Limits
# -----------------------------

MIN_CHOKE = 0.0
MAX_CHOKE = 100.0
INITIAL_CHOKE = 30.0
MAX_CHOKE_STEP = 5.0

# -----------------------------
# Pressure Limits
# -----------------------------

MIN_WHP = 40.0
MAX_WHP = 120.0

MIN_FLP = 20.0
MAX_FLP = 100.0

MIN_BHP = 150.0
MAX_BHP = 350.0

# -----------------------------
# Controller Settings
# -----------------------------

FLOW_TOLERANCE = 2.0
MAX_ITERATIONS = 300
CONTROL_INTERVAL = 1

# -----------------------------
# Logging
# -----------------------------

ENABLE_LOGGING = True