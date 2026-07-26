"""
controller.py
Constraint-aware Autonomous Choke Controller
"""

import config
from optimizer import ChokeOptimizer
from constraints import ConstraintChecker


class AutonomousController:

    def __init__(self):
        self.current_choke = config.INITIAL_CHOKE

    def control(self, measurements, target_flow):

        candidate = ChokeOptimizer.propose(
            self.current_choke,
            measurements,
            target_flow
        )

        if ConstraintChecker.pressure_safe(
            measurements["whp"],
            measurements["flp"],
            measurements["bhp"]
        ) and ConstraintChecker.choke_safe(
            self.current_choke,
            candidate
        ):
            self.current_choke = candidate

        return self.current_choke