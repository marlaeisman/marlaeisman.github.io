---
layout: default
title: "RACER: Learned Residual Dynamics for Wheeled-Quadruped Racing"
permalink: /racer/
---

# RACER: Learned Residual Dynamics for Sampling-Based Racing (2026)

**Paper:** "RACER: Residual-Adaptive Closed-Loop Estimation for Sampling-Based Planning in Wheeled-Quadruped Racing." *Submitted to ICRA 2027.* 

**Keywords:** MPPI · sampling-based MPC · learned residual dynamics · low-rank adaptation · sim-to-real · hierarchical RL · Unitree Go2W

<img src="/images/racer_hardware.jpg" alt="Time-lapse composite of a Unitree Go2W racing around an L-shaped indoor track with RACER" width="100%" style="height:auto;" />

### What's new

- **Planner–tracker model:** a sampling-based planner commands an RL velocity tracker. The planner usually assumes those commands are tracked perfectly, which breaks down in fast corners. RACER instead learns the tracker's closed-loop error as a residual on a simple kinematic model.
- **LoRRA (Low-Rank Residual Adaptation):** the residual is pre-trained in simulation, then adapted to the real robot with a low-rank update from a few hundred real transitions. The real data corrects the model without erasing what it learned in simulation.

### Results on hardware

- **Speed:** RACER completed every lap at every velocity cap up to 3.2 m/s and got faster as the cap rose (1.95 m/s average). The same planner with a kinematic model completed **zero** laps at 2.0 m/s and above.
- **Robustness to sim-to-real gap:** as the gap widened, LoRRA kept completing laps (2.3 of 3 at the largest gap). Full fine-tuning failed completely and training on real data alone failed at almost every gap.
- **Simulation:** LoRRA's advantage grows with the size of the domain gap, across friction and joint-gain shifts.

<img src="/images/racer_vs_unicycle_hw.jpg" alt="Hardware frames at a 3.2 m/s cap: kinematic-model planner fails at the first corner while RACER passes it" width="100%" style="height:auto;" />

*3.2 m/s cap. Top: the kinematic-model planner fails at the first corner. Bottom: RACER takes it cleanly.*

<img src="/images/racer_prediction_error.jpg" alt="Next-state prediction error along the track for RACER and the kinematic model" width="100%" style="height:auto;" />

*Prediction error around the track. The kinematic model's error spikes in fast corners, where all of its failures (×) happen. RACER's stays low around the whole lap.*

**Stack:** PyTorch, MuJoCo, Isaac Lab / RSL-RL, CasADi, ROS 2.

Related: [roll-control MPC for wheeled-quadruped racing (AVEC 2026)]({{ '/wheeled-quadruped/' | relative_url }}).
