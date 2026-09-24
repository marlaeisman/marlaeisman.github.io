---
layout: default

title: "Enhanced Target Tracking Using Real-Time Residual Neural Networks"
permalink: /ResNet/
---

# Enhanced Target Tracking Using Real-Time Residual Neural Networks (2024)

**Summary:**
Developed and analyzed a residual neural network (ResNet) architecture for real-time quadrotor target tracking, integrating learning-based control with sensor fusion for robust outdoor operation.

**Key results & publications:**
- Thesis: "Enhanced Target Tracking Using Real-Time Residual Neural Networks" (2024).
- Peer-reviewed: C.F. Nino, O. Sudhir Patil, J.C. Insinger, **M.R. Eisman**, and W.E. Dixon, "Online ResNet-Based Adaptive Control for Nonlinear Target Tracking," *IEEE Control Systems Letters*, presented at the IEEE Conference on Decision and Control (CDC), 2025.

**Technical details:**
- Sensor fusion: GPS, IMU, and LiDAR fused in ROS 2; control and estimator pipelines implemented in C++/Python.
- Theoretical correspondence: designed Lyapunov-style stability proofs and validated that simulation metrics matched experimental behavior.

<img src="/images/drone.gif" width="100%" style="height:auto;" />
<img src="/images/sim.gif" width="100%" style="height:auto;" />
