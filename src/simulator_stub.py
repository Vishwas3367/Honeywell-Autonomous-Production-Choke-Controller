"""
simulator_stub.py
Dummy simulator for testing the Autonomous Production Choke Controller.

This file simulates the behaviour of a naturally flowing oil well.
"""

import random


class OilWellSimulator:

    def __init__(self):

        self.choke = 30.0
        self.flow = 80.0
        self.whp = 90.0
        self.flp = 45.0
        self.bhp = 280.0

        # Reservoir decline
        self.decline = 0.0

    def step(self, new_choke):

        # Limit choke
        self.choke = max(0.0, min(100.0, new_choke))

        # -----------------------------
        # Disturbance 1: Reservoir Decline
        # -----------------------------
        self.decline += 0.05

        # -----------------------------
        # Disturbance 2: Sensor Noise
        # -----------------------------
        flow_noise = random.uniform(-3, 3)
        pressure_noise = random.uniform(-1.5, 1.5)

        # -----------------------------
        # Well Model
        # -----------------------------
        self.flow = (2.5 * self.choke) - self.decline + flow_noise

        self.whp = 120 - 0.35 * self.choke + pressure_noise
        self.flp = 20 + 0.40 * self.choke + pressure_noise
        self.bhp = 320 - 0.60 * self.choke + random.uniform(-2, 2)

        # -----------------------------
        # Disturbance 3: Pressure Spike
        # -----------------------------
        if random.random() < 0.05:
            self.whp += 8
            print(">>> Disturbance: Temporary WHP Spike")

        return {
            "flow": self.flow,
            "whp": self.whp,
            "flp": self.flp,
            "bhp": self.bhp,
            "choke": self.choke
        }