"""
optimizer.py
Simplified Predictive Choke Optimizer
"""

from constraints import ConstraintChecker


class ChokeOptimizer:

    LAMBDA = 0.2

    @staticmethod
    def predict(choke):

        flow = 2.5 * choke

        # Match your simulator equations
        whp = 120 - 0.35 * choke
        flp = 20 + 0.40 * choke
        bhp = 320 - 0.60 * choke

        return {
            "flow": flow,
            "whp": whp,
            "flp": flp,
            "bhp": bhp
        }

    @staticmethod
    def propose(current_choke, measurements, target_flow):

        best_choke = current_choke
        best_cost = float("inf")

        for candidate in range(0, 101, 5):

            prediction = ChokeOptimizer.predict(candidate)

            if not ConstraintChecker.pressure_safe(
                prediction["whp"],
                prediction["flp"],
                prediction["bhp"]
            ):
                continue

            # Respect maximum choke movement
            if not ConstraintChecker.choke_safe(
                current_choke,
                candidate
            ):
                continue

            production_error = abs(
                target_flow - prediction["flow"]
            )

            movement_penalty = abs(
                candidate - current_choke
            )

            cost = (
                production_error
                + ChokeOptimizer.LAMBDA * movement_penalty
            )

            if cost < best_cost:
                best_cost = cost
                best_choke = candidate

        return best_choke