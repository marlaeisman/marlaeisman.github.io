---
layout: home
---

## About Me

I'm a PhD student in Mechanical Engineering (Controls) at UC Berkeley in Prof. Francesco Borrelli's [MPC Lab](https://sites.google.com/berkeley.edu/mpc-lab). I build learning-based control for legged-wheeled robots, combining reinforcement learning, model predictive control and onboard perception, and I take it from GPU simulation to real hardware. On the Unitree Go2W I train locomotion policies in Isaac Lab, learn dynamics models for GPU-parallel MPPI racing, and run perception-driven control onboard a Jetson Orin.

Previously: B.S. Mechanical Engineering, University of Florida (2024); researcher in UF's [Nonlinear Controls and Robotics Lab](https://ncr.mae.ufl.edu/); Lead Engineer at [Gator Motorsports](https://gatormotorsports.org/); internships at [SpaceX](https://www.spacex.com/), [Tesla](https://www.tesla.com/) and [Vatn Systems](https://www.vatnsystems.com/).

---

### Blog
<div class="projects-scroll">
  <div class="project-card blog-card">
  <ul class="blog-list">
  {%- for post in site.data.blog %}
    <li><a href="{{ post.url | relative_url }}"><strong>{{ post.title }}</strong></a> <span class="project-date">· {{ post.date }}</span><br />{{ post.summary }}</li>
  {%- endfor %}
  </ul>
    <div class="project-meta">
      <span class="project-date">{{ site.data.blog | size }} posts</span>
  <a class="read-more" href="{{ '/blog/' | relative_url }}">All posts →</a>
    </div>
  </div>
</div>

---

### Skills
- **Robot learning:** deep RL (PPO), sim-to-real transfer, learned dynamics models, low-rank adaptation, CNNs
- **Control and planning:** MPC, MPPI and sampling-based planning, trajectory optimization, system identification
- **Perception:** RGB-D terrain estimation, camera–IMU calibration, lidar-inertial odometry, sensor fusion
- **Tools:** Python, C++, PyTorch, Isaac Lab / Isaac Sim, MuJoCo, ROS 2, NVIDIA Jetson Orin, CasADi, OSQP

---

### Publications
- **Racing a Wheeled Quadruped: Active Load Transfer Mitigation via Model Predictive Control.** **M. Eisman**, B. Lam, S. Sonnino, F. Borrelli. *AVEC 2026.* [Page]({{ '/wheeled-quadruped/' | relative_url }}) · [Code](https://github.com/meisman-ucb/go2w-roll-control-mpc)
- **RACER: Residual-Adaptive Closed-Loop Estimation for Sampling-Based Planning in Wheeled-Quadruped Racing.** *Under review, ICRA 2027.* [Page]({{ '/racer/' | relative_url }})
- **Online ResNet-Based Adaptive Control for Nonlinear Target Tracking.** *IEEE Control Systems Letters*, presented at CDC 2025. [Page]({{ '/ResNet/' | relative_url }})

---

### News
- **2026:** [RACER]({{ '/racer/' | relative_url }}), MPPI racing with learned residual dynamics, submitted to ICRA 2027.
- **2026:** Presented [Racing a Wheeled Quadruped]({{ '/wheeled-quadruped/' | relative_url }}) at AVEC 2026 in Tsukuba, Japan. [Read about the trip →]({{ '/blog/avec-2026/' | relative_url }})
- **2025:** [Online ResNet-Based Adaptive Control for Nonlinear Target Tracking]({{ '/ResNet/' | relative_url }}) published in IEEE Control Systems Letters and presented at CDC 2025.
- **2025:** Started my PhD at UC Berkeley with the First-Year Fellowship.

