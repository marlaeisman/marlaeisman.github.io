## About Me

I'm a PhD student in Mechanical Engineering (Controls) at UC Berkeley in Prof. Francesco Borrelli's [MPC Lab](https://sites.google.com/berkeley.edu/mpc-lab). I build learning-based control for legged-wheeled robots, combining reinforcement learning, model predictive control and onboard perception, and I take it from GPU simulation to real hardware. On the Unitree Go2W I train locomotion policies in Isaac Lab, learn dynamics models for GPU-parallel MPPI racing, and run perception-driven control onboard a Jetson Orin.

Previously: B.S. Mechanical Engineering, University of Florida (2024); researcher in UF's [Nonlinear Controls and Robotics Lab](https://ncr.mae.ufl.edu/); Lead Engineer at [Gator Motorsports](https://gatormotorsports.org/); internships at [SpaceX](https://www.spacex.com/), [Tesla](https://www.tesla.com/) and [Vatn Systems](https://www.vatnsystems.com/).

---

### Blog
<div class="projects-scroll">
  <div class="project-card blog-card">
  <ul class="blog-list">
  {% for post in site.data.blog %}
    <li><a href="{{ post.url | relative_url }}"><strong>{{ post.title }}</strong></a> <span class="project-date">· {{ post.date }}</span><br />{{ post.summary }}</li>
  {% endfor %}
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

---

### Projects
<div class="projects-scroll">
  <div class="project-card">
  <img src="/images/racer_hardware.jpg" alt="Time-lapse of a Unitree Go2W racing an indoor track with RACER" />
  <h3>RACER: Learned Residual Dynamics for Quadruped Racing</h3>
  <p>Learns how an RL locomotion policy actually tracks commands, so a GPU-parallel MPPI planner can race on it. A low-rank sim-to-real adaptation needs only a few hundred real samples. On hardware: every lap completed up to 3.2 m/s, where the kinematic baseline completed none. Submitted to ICRA 2027.</p>
  <div class="tags"><span class="tag">MPPI</span><span class="tag">learned dynamics</span><span class="tag">low-rank adaptation</span><span class="tag">sim-to-real</span><span class="tag">PyTorch</span></div>
    <div class="project-meta">
      <span class="project-date">2026</span>
  <a class="read-more" href="{{ '/racer/' | relative_url }}">Read more →</a>
    </div>
  </div>
  <div class="project-card">
  <img src="/images/nonplanar_stack.svg" alt="Pipeline from depth camera to terrain lookahead, roll MPC, lean interface and RL policy" style="object-fit:contain;" />
  <h3>Perception-Driven Roll Control on Nonplanar Terrain</h3>
  <p>Depth camera + IMU see terrain bank up to 3 m ahead. A sub-millisecond MPC leans the robot into it through an Isaac Lab PPO locomotion policy without retraining. The full loop runs onboard a Jetson Orin. 77% less cornering load transfer in simulation.</p>
  <div class="tags"><span class="tag">RGB-D perception</span><span class="tag">sensor fusion</span><span class="tag">Isaac Lab</span><span class="tag">PPO</span><span class="tag">MPC</span><span class="tag">Jetson Orin</span></div>
    <div class="project-meta">
      <span class="project-date">2026–</span>
  <a class="read-more" href="{{ '/nonplanar-terrain/' | relative_url }}">Read more →</a>
    </div>
  </div>
  <div class="project-card">
  <video src="/images/roll.mp4" autoplay loop muted playsinline aria-label="Unitree Go2W racing with active roll control"></video>
  <h3>Racing a Wheeled Quadruped: Active Load Transfer Mitigation via Model Predictive Control</h3>
  <p>MPC that races a Unitree Go2W on a minimum-time raceline while using its legs to roll the body against lateral load transfer. Validated on hardware. AVEC 2026, <a href="https://github.com/meisman-ucb/go2w-roll-control-mpc">code on GitHub</a>.</p>
  <div class="tags"><span class="tag">MPC</span><span class="tag">raceline optimization</span><span class="tag">vehicle dynamics</span><span class="tag">hardware</span></div>
    <div class="project-meta">
      <span class="project-date">2026</span>
  <a class="read-more" href="{{ '/wheeled-quadruped/' | relative_url }}">Read more →</a>
    </div>
  </div>
  <div class="project-card">
  <img src="/images/dog.gif" alt="Unitree Go2W with lidar on the lab track" />
  <h3>Go2W Research Platform</h3>
  <p>The lab's ROS 2 stack for the Go2W: a 500 Hz C++ joint bridge, onboard RL policy deployment, MPC and MPPI nodes, and fused motion capture, lidar and RGB-D sensing.</p>
  <div class="tags"><span class="tag">ROS 2</span><span class="tag">C++</span><span class="tag">real-time control</span><span class="tag">sensor fusion</span><span class="tag">deployment</span></div>
    <div class="project-meta">
      <span class="project-date">2025–</span>
  <a class="read-more" href="{{ '/go2w-platform/' | relative_url }}">Read more →</a>
    </div>
  </div>
  <div class="project-card">
  <img src="/images/vatn.gif" alt="AUV" />
  <h3>AUV Autonomy</h3>
  <p>Model-based LQR controllers and navigation stacks for AUVs. Contributed to Vatn’s first multi-AUV swarm demonstration using acoustic communication and DVL feedback for coordinated stability.</p>
  <div class="tags"><span class="tag">LQR</span><span class="tag">navigation</span><span class="tag">multi-agent</span><span class="tag">marine robotics</span></div>
    <div class="project-meta">
      <span class="project-date">2025</span>
  <a class="read-more" href="{{ '/vatn/' | relative_url }}">Read more →</a>
    </div>
  </div>
  <div class="project-card">
  <img src="/images/drone.gif" alt="ResNet Project Drone" />
  <h3>Enhanced Target Tracking Using Real-Time Residual Neural Networks</h3>
  <p>Developed and mathematically analyzed a custom ResNet architecture for real-time quadrotor tracking (thesis, 2024). Resulting work was published as "Online ResNet-Based Adaptive Control for Nonlinear Target Tracking" in IEEE Control Systems Letters and presented at IEEE CDC (2025).</p>
  <div class="tags"><span class="tag">ResNet</span><span class="tag">adaptive control</span><span class="tag">Lyapunov analysis</span><span class="tag">quadrotor</span></div>
    <div class="project-meta">
      <span class="project-date">2024–2025</span>
  <a class="read-more" href="{{ '/ResNet/' | relative_url }}">Read more →</a>
    </div>
  </div>
  <div class="project-card">
  <img src="/images/herding.gif" alt="DNN Herding Simulation" />
  <h3>Adaptive Multi-Agent Herding With Deep Neural Networks</h3>
  <p>Built a Python-based simulator and recursive parameter-sweep framework (depth, learning rate, activations) producing quantitative error curves and convergence metrics; validated learned controllers in outdoor real-time experiments.</p>
  <div class="tags"><span class="tag">deep learning</span><span class="tag">multi-agent</span><span class="tag">simulation</span></div>
    <div class="project-meta">
      <span class="project-date">2023–2024</span>
  <a class="read-more" href="{{ '/DNN/' | relative_url }}">Read more →</a>
    </div>
  </div>
  <div class="project-card">
  <img src="/images/gms.png" alt="Gator Motorsports EV" />
  <h3>UF's First Electric Formula-Style Vehicle</h3>
  <p>Led design/manufacture of UF’s first EV Formula SAE car: secured $70,000 in sponsorships, designed a 400V battery powertrain, manufactured 90% of components in-house, and finished 3rd overall at Formula SAE Michigan 2022 (1st Acceleration).</p>
  <div class="tags"><span class="tag">EV powertrain</span><span class="tag">vehicle design</span><span class="tag">team lead</span></div>
    <div class="project-meta">
      <span class="project-date">2020–2023</span>
  <a class="read-more" href="{{ '/GMS/' | relative_url }}">Read more →</a>
    </div>
  </div>
  <div class="project-card">
  <img src="/images/swe.jpg" alt="Volunteer Work" />
  <h3>Volunteer Work</h3>
  <p>STEM outreach (2+ events/semester), Habitat for Humanity construction support, and weekly hospice volunteering (30+ hours in the last year).</p>
    <div class="project-meta">
      <span class="project-date">2020–2024</span>
  <a class="read-more" href="{{ '/volunteer/' | relative_url }}">Read more →</a>
    </div>
  </div>
</div>
---
