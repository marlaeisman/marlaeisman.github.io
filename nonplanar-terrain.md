---
layout: default
title: "Perception-Driven Roll Control on Nonplanar Terrain"
permalink: /nonplanar-terrain/
---

# Perception-Driven Roll Control on Nonplanar Terrain (2026– )

*Ongoing PhD research. I lead the project and supervise the undergraduate researchers working on it.*

**Keywords:** RGB-D perception · sensor fusion · camera–IMU calibration · deep RL (PPO) · Isaac Lab · sim-to-real · convex MPC · ROS 2 · Jetson Orin · Unitree Go2W

<img src="/images/nonplanar_stack.svg" alt="Pipeline from depth camera and IMU to terrain lookahead, roll MPC, lean interface and RL locomotion policy" width="100%" style="height:auto;" />

### Goal

My [AVEC 2026 paper]({{ '/wheeled-quadruped/' | relative_url }}) used the legs to roll a wheeled quadruped's body against lateral load transfer on flat ground. This project takes the idea to ramps, cross-sloped streets and a skate park. On those surfaces the robot has to see a bank coming and lean before it reaches it.

### What's new

- **Seeing the terrain ahead:** a depth camera fused with the IMU estimates surface bank up to 3 m ahead. It runs onboard in real time with 0.03° standing noise, and it tracked a measured 6–8° street slope as the robot changed heading.
- **Planning the lean:** a convex MPC plans body lean ahead of time to minimize load transfer, and solves in under 1 ms onboard.
- **No retraining:** the MPC steers an RL locomotion policy through a lean interface that leaves the policy's weights untouched. With the MPC off, the robot behaves exactly as before.
- **Locomotion:** a PPO policy trained on 4,096 parallel GPU environments in Isaac Lab. In cross-simulator tests it drives 0–2 m/s on flat ground and a skate-park model with zero flips.

### Results

- **Simulation:** in a sustained 2 m/s turn, 77% less steady cornering load transfer. Load measured at the wheels fell 70–80% in carving, with only an 8% cost in tracking.
- **Locomotion policy:** velocity-tracking error 0.12 → 0.07 m/s and standing heading drift −152° → −4.5° against the previous policy.
- **Hardware:** the full perception → MPC → RL loop runs onboard a Jetson Orin, with zero solver failures over 5,000+ onboard solves. The robot leans live while driving, and the simulated lean response matched hardware within 7%.
- **Calibration:** I found and removed a 4° camera mount bias using a procedure that needs no level ground.

Outdoor banking runs on sloped streets and a skate park are underway.

**Stack:** Python, PyTorch, Isaac Lab, RSL-RL, MuJoCo, OSQP, ROS 2, Intel RealSense, NVIDIA Jetson Orin.
