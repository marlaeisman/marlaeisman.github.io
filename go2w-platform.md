---
layout: default
title: "Go2W Research Platform: ROS 2 Stack for a Wheeled Quadruped"
permalink: /go2w-platform/
---

# Go2W Research Platform: ROS 2 Stack for a Wheeled Quadruped (2025– )

*MPC Lab, UC Berkeley. I built and maintain the lab's Unitree Go2W software stack.*

**Keywords:** ROS 2 · C++ · Python · DDS · real-time control · sensor fusion · motion capture · lidar-inertial odometry · RGB-D · policy deployment

<img src="/images/dog.gif" alt="Unitree Go2W with roof-mounted lidar driving on the lab track" width="100%" style="height:auto;" />

The platform replaces the Go2W's stock locomotion controller with our own, from joint commands up to planners, with the vendor safety layer kept as a fallback. Every robot project on this site runs on it: [roll-control MPC]({{ '/wheeled-quadruped/' | relative_url }}), [RACER]({{ '/racer/' | relative_url }}) and [perception-driven roll control]({{ '/nonplanar-terrain/' | relative_url }}).

- **Real-time control:** a C++ / DDS joint bridge at 500 Hz, with rate limiting, an e-stop and a safe hand-back to the vendor controller.
- **Sensing:** OptiTrack motion capture, lidar-inertial odometry (FAST-LIO2), RealSense RGB-D and wheel odometry, with synchronized multi-sensor logging for datasets.
- **Learned-policy deployment:** RL policies run onboard at 50 Hz, with an automated check that hardware inputs match simulation before every session.
- **Planners:** raceline MPC, MPPI and roll-control MPC nodes, plus teleoperation.
- **Simulation:** cross-validated MuJoCo and Isaac Lab models that share controller code with the robot.

It is the lab's shared testbed for reproducible controller comparisons, and the undergraduate researchers I mentor build on it.

**Stack:** ROS 2, C++, Python, CycloneDDS, Unitree SDK2, PyTorch, MuJoCo, Isaac Lab, OptiTrack, Hesai lidar, FAST-LIO2, Intel RealSense, NVIDIA Jetson Orin.
