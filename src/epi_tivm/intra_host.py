import numpy as np
from scipy.integrate import solve_ivp

class WithinHostTIVMSolver:
    """
    Target-Infected-Virus-Macrophage (TIVM) ODE Solver for Intra-Host Viral Dynamics.
    """
    def __init__(self, beta_v=1e-5, p=100.0, c=2.0, k_m=1e-4, delta_i=0.5):
        self.beta_v = beta_v
        self.p = p
        self.c = c
        self.k_m = k_m
        self.delta_i = delta_i

    def deriver(self, t, y):
        T, I, V, M = y
        dT = -self.beta_v * T * V
        dI = self.beta_v * T * V - self.delta_i * I
        dV = self.p * I - self.c * V - self.k_m * M * V
        dM = 0.1 * V - 0.05 * M
        return [dT, dI, dV, dM]

    def solve(self, t_span=(0, 30), y0=[1e6, 0.0, 1.0, 1e3]):
        sol = solve_ivp(self.deriver, t_span, y0, method='Radau', dense_output=True)
        return sol
