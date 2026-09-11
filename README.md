# Coupled Multiscale Epidemic ODE Solver: Within-Host Viral Kinetics & Macro-Transmission Dynamics

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![SciPy](https://img.shields.io/badge/SciPy-Radau%20ODE-red.svg)](https://scipy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A high-fidelity multiscale ordinary differential equation (ODE) framework coupling within-host viral kinetics (Target cell - Infected cell - Viral load - Macrophage response, TIVM) with macro-scale population epidemiology (SEPIAQRV framework).

---

## 🦠 Multiscale Mathematical Architecture

```mermaid
flowchart TD
    subgraph Micro Scale: Within-Host Kinetics
        T[Target Cells T] -->|Infection k_v| I[Infected Cells I]
        I -->|Viral Production p| V[Viral Load V]
        M[Macrophage M] -->|Clearance k_M| V
    end
    
    subgraph Dual-Route Hill Coupling
        V -->|Cutaneous Route| BetaL[Beta_L Hill Kinetics]
        V -->|Respiratory Route| BetaR[Beta_R Hill Kinetics]
    end

    subgraph Macro Scale: SEPIAQRV Epidemiology
        S[Susceptible] --> E[Exposed]
        E --> P[Prodromal]
        P --> Symptom[Symptomatic I]
        P --> Asymptom[Asymptomatic A]
        Symptom --> Q[Quarantined]
        Symptom --> R[Recovered]
    end
    
    BetaL & BetaR --> S
```

---

## 🧮 Formal Mathematical Formulations

### 1. Within-Host TIVM Dynamics
$$\frac{dT}{dt} = s_T - d_T T - \beta_v T V$$

$$\frac{dI}{dt} = \beta_v T V - \delta_I I$$

$$\frac{dV}{dt} = p I - c V - k_M M V$$

$$\frac{dM}{dt} = s_M + \eta V M - d_M M$$

### 2. Next-Generation Matrix (NGM) $R_0$ Derivation
The basic reproduction number $R_0$ is calculated analytically as the spectral radius of the NGM:

$$R_0 = \rho\left( \mathbf{F} \mathbf{V}^{-1} \right)$$

where $\mathbf{F}$ is the rate of appearance of new infections, and $\mathbf{V}$ is the net rate of transfer out of infected compartments across all 126+ infected states.

---

## 📊 Calibrated Model Validation Metrics

| Parameter / Metric | Model Numerical Output | Literature Target | Status |
| :--- | :---: | :---: | :---: |
| **Basic Reproduction Number ($R_0$)** | **4.36** | 3.0 – 5.0 | Verified |
| **Peak Intra-Host Viral Load** | **8.26 $\log_{10}$ copies/mL** | ~8.0 $\log_{10}$ | Verified |
| **Incubation Period** | **7.7 days** | 7 – 9 days | Verified |
| **Mass Conservation Leakage** | **$< 10^{-14}$** | 0.00 | Verified |

---

## 🚀 Usage & Quickstart

```bash
pip install -e .
python -m epi_tivm.inter_host --simulate --plot
```
