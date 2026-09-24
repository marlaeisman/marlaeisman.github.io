---
layout: default

title: "MPC Lab: Model Predictive Control and Reinforcement Learning for Legged Robots"
permalink: /mpc/
---

# MPC Lab: Model Predictive Control and Reinforcement Learning for Legged Robots (2025– )

**Summary:**
PhD research focused on developing and analyzing model predictive control (MPC) and reinforcement learning algorithms for agile legged robots (Unitree Go2W). Emphasis on robust trajectory planning, optimal feedback control, and real-world deployment in uncertain environments.

**Key results:**
- Developed an MPC for racing a wheeled quadruped with active load transfer mitigation, published at AVEC 2026 ([paper page]({{ '/wheeled-quadruped/' | relative_url }}) · [code](https://github.com/meisman-ucb/go2w-roll-control-mpc)).
- Integrated the Unitree Go2W into a modular ROS 2 interface and developed an open-source, lab-wide evaluation platform that combines motion-capture data with on-board state estimation for reproducible controller benchmarks.
- Applied MPC and RL methods to energy management, raceline optimization, and obstacle-stability scenarios and validated methods in both simulation and hardware.

**Technical details:**
- Implementation: ROS 2, Python and C/C++ control modules, motion-capture integration, and standardized benchmark scenarios for controller evaluation.
- Reproducibility: modular ROS 2 nodes, documented parameter sets, and automated experiment scripts to allow repeatable lab-wide comparisons.

<img src="/images/dog.gif" width="100%" style="height:auto;" />
