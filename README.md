<p align="center">
<h1 align="center"<strong> Risk-Aware Autonomous Driving with Linear Temporal Logic Specifications </strong>
</h1>
  <p align="center">
    Shuhao Qi<sup>1</sup>, Zengjie Zhang <sup>1</sup>, Zhiyong Sun<sup>2</sup> and Sofie Haesaert<sup>1</sup>
    <br>
    <sup>1</sup> Eindhoven University of Technology <sup>2</sup> Peking University
    <br>
  </p>
</p>

<p align="center">
  <a href='https://arxiv.org/abs/2409.09769'>
    <img src='https://img.shields.io/badge/Arxiv-2409.09769-A42C25?style=flat&logo=arXiv&logoColor=A42C25'></a>
  <a href='https://www.youtube.com/watch?v=r5kEMW8oPQE'>
    <img src='https://img.shields.io/youtube/views/r5kEMW8oPQE'></a>
</p>

## Overview

This repository provides a minimal example of the risk-aware planning framework proposed 
in the paper: [ArXiv:2409.09769](https://arxiv.org/abs/2409.09769), without relying on Carla. 
This example is designed to help users understand the proposed framework in a simplified setting.

## Repository Structure

- `reactive_LTL_main.py` - Main script handling reactive Linear Temporal Logic (LTL) computations.

### Abstraction Module (`abstraction/`)
- `abstraction.py` - Implements abstraction mechanisms for system modeling.
- `MDP.py` - Defines a Markov Decision Process (MDP) abstraction.
- `prod_MDP.py` - Implements a product MDP for combining different abstractions.

### Risk-aware Linear Programming Module (`risk_LP/`)
- `risk_LP.py` - Risk-aware linear programming (LP) problems.
- `ltl_risk_LP.py` - Implements risk-aware LP methods under LTL constraints.
- `prod_auto.py` - Construct product automaton.
- `risk_field_plot.py` - Provides visualization tools for risk field data.

### Simulation Module (`sim/`)
- `simulator.py` - Simulates the environment and vehicle dynamic.
- `perception.py` - Analog perception module to provide sensor information.
- `visualizer.py` - PLot simulation results.
- `controller.py` - Low-level MPC controller for the bicycle model.

### Specification Module (`specification/`)
- `specification.py` - Translate LTL specifications.
- `DFA.py` - Define deterministic finite automata (DFA).

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- Required dependencies: `Gurobi`, `numpy`, `matplotlib`, `networkx`, and `scipy`.

### Quick Start

Run the main script:
```bash
python reactive_LTL_main.py
```

## License

This project is licensed under the MIT License. Please consider citing our papers if the project helps your research with the following BibTex:

```bibtex
@INPROCEEDINGS{qi2025risk,
  author={Qi, Shuhao and Zhang, Zengjie and Sun, Zhiyong and Haesaert, Sofie},
  booktitle={2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)}, 
  title={Risk-Aware Autonomous Driving with Linear Temporal Logic Specifications}, 
  year={2025},
  pages={14877-14883}}
```

