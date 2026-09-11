# Coupled Multi-Scale Epidemic ODE Solver for Monkeypox (MPXV)
The Multiscale-Epi-TIVM framework is a computational biology model that effectively bridges within-host viral kinetics (Target cell-Infected cell-Virus-Macrophage, or TIVM) with macroscopic population transmission.


[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![SciPy](https://img.shields.io/badge/SciPy-ODE-red.svg)](https://scipy.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()

> **A high-fidelity, multi-scale compartmental model simulating Monkeypox (Clade IIb) transmission dynamics, integrating within-host viral kinetics, dual-route macro-scale transmission, and advanced behavioral/environmental modifiers.**

## Overview

This repository contains a sophisticated Ordinary Differential Equation (ODE) framework designed to model the spread of Monkeypox. Unlike traditional SIR models, this solver couples **micro-scale within-host viral dynamics** with **macro-scale population epidemiology**. It features a 134-state unified architecture that accurately captures clinical progression, asymptomatic spread, environmental fomite transmission, and dynamic human behavioral responses.

This project demonstrates advanced proficiency in computational epidemiology, numerical methods for stiff ODEs, and object-oriented software design for scientific computing.

---

## Model Architecture

The model is structured into four distinct, interconnected layers:

### Layer 1: Within-Host Viral Kinetics (Micro-Scale)
Utilizes a Target-Infected-Virus-Immune (TIVM) model to simulate the biological progression of MPXV within an individual:
*   **States:** Susceptible Target Cells ($T$), Infected Cells ($I$), Viral Load ($V$), Immune Effectors ($M$).
*   **Dynamics:** Governs viral production, immune-mediated neutralization, and target cell depletion, generating a time-dependent viral shedding profile $V(\tau)$.

### Layer 2: Dual-Route Transmission Coupling
Maps the within-host viral load to population-level infectiousness via two distinct pathways:
*   **Cutaneous Route ($V_L$):** Dominant transmission via skin lesions (higher $\beta_{max}$, higher EC50 threshold).
*   **Respiratory Route ($V_R$):** Secondary transmission via respiratory droplets (lower $\beta_{max}$, lower EC50 threshold).
*   Uses Hill equations to dynamically scale transmission probability based on real-time viral load.

### Layer 3: Clinical Granularity & Cohort Tracking (Macro-Scale)
Expands standard compartmental models into a highly granular **SEPIAQRV** framework, stratified by High-Risk and Low-Risk behavioral groups:
*   **Compartments:** Susceptible ($S$), Exposed ($E$), Prodromal ($P$), Symptomatic ($I$), Asymptomatic ($A$), Quarantined ($Q$), Recovered ($R$), Vaccinated ($V_v$).
*   **Cohort Chain:** Implements a $K=60$ discrete cohort chain for the Symptomatic ($I$) compartment to accurately model the fixed-duration infectious period without the unrealistic exponential decay of standard ODEs.

### Layer 4: Advanced Real-World Modifiers
*   **Prevalence-Elastic Mixing:** Dynamic contact matrices where high-risk individuals reduce contact rates as cumulative case counts rise.
*   **Legacy Cross-Immunity:** A dampening coefficient ($\lambda = 0.85$) protecting older cohorts with historical smallpox vaccination.
*   **Environmental Reservoirs ($F_{env}$):** Models indirect fomite transmission via shedding rates ($\xi$) and environmental decay constants ($\mu_{env}$).

---

## Mathematical & Computational Rigor

*   **Next-Generation Matrix (NGM) for $R_0$:** Analytically derives the Basic Reproduction Number by calculating the spectral radius ($\rho$) of the $FV^{-1}$ matrix across all 126+ infected states, ensuring mathematical consistency with the ODE system.
*   **Stiff ODE Integration:** Utilizes `scipy.integrate.solve_ivp` with the **Radau** implicit method, specifically chosen for its stability in handling the stiff, multi-scale nature of coupled viral-immune-epidemic systems.
*   **Mass Conservation:** Rigorous assertion checks ensure zero population leakage across all 134 state variables throughout the simulation timeline.

---

## Software Engineering Highlights

*   **Dynamic State Mapping:** Replaced brittle, hardcoded array indexing with an object-oriented `StateMap` class. This allows for safe, scalable addition of new compartments (e.g., environmental reservoirs, cumulative trackers) without breaking derivative calculations.
*   **Vectorized Operations:** Leverages NumPy vectorization for cohort chain transitions and force-of-infection calculations, ensuring high computational performance.
*   **Modular Design:** Clear separation of parameter definitions, ODE right-hand side functions, and visualization logic, adhering to clean code principles.

---

## Key Validation Metrics

The model is calibrated against literature estimates for the 2022-2026 Clade IIb outbreak:
| Metric | Model Output | Literature Target |
| :--- | :---: | :---: |
| **Basic Reproduction Number ($R_0$)** | ~4.36 | 3.0 - 5.0 |
| **Peak Within-Host Viral Load** | ~8.26 log10 copies/mL | ~8.0 log10 |
| **Incubation Period** | ~7.7 days | 7 - 9 days |
| **High-Risk Attack Rate** | ~31.8% | Context-dependent |
| **Low-Risk Attack Rate** | ~5.0% | Context-dependent |

---

## Installation & Usage

### Prerequisites
Ensure you have Python 3.8+ installed. Install the required dependencies:
```bash
pip install numpy scipy matplotlib pandas seaborn
