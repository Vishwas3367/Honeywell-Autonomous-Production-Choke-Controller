"""
constraints.py
Checks whether the controller action is safe.
"""

import config


class ConstraintChecker:

    @staticmethod
    def pressure_safe(whp, flp, bhp):

        if whp < config.MIN_WHP:
            return False

        if whp > config.MAX_WHP:
            return False

        if flp < config.MIN_FLP:
            return False

        if flp > config.MAX_FLP:
            return False

        if bhp < config.MIN_BHP:
            return False

        if bhp > config.MAX_BHP:
            return False

        return True

    @staticmethod
    def choke_safe(current_choke, new_choke):

        if new_choke < config.MIN_CHOKE:
            return False

        if new_choke > config.MAX_CHOKE:
            return False

        movement = abs(new_choke - current_choke)

        if movement > config.MAX_CHOKE_STEP:
            return False

        return True