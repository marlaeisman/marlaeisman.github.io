---
layout: default
title: "Wheeled Quadruped Robot Control"
permalink: /wheeled-quadruped/
---

# Wheeled Quadruped Robot Control (2026)

<video src="/images/roll.mp4" autoplay loop muted playsinline aria-label="Unitree Go2W racing with active roll control" width="100%" style="height:auto;"></video>

**Paper:** "Racing a Wheeled Quadruped: Active Load Transfer Mitigation via Model Predictive Control." **M. Eisman**, B. Lam, S. Sonnino, and F. Borrelli. *17th International Symposium on Advanced Vehicle Control (AVEC)*, 2026.

[**Code & videos on GitHub**](https://github.com/meisman-ucb/go2w-roll-control-mpc) · [Presenting at AVEC 2026 in Japan]({{ '/blog/avec-2026/' | relative_url }})

**Keywords:** model predictive control · nonlinear optimization · minimum-time raceline · vehicle dynamics · load transfer · legged-wheeled robots

**Summary:**
Wheeled quadrupeds like the Unitree Go2W can drive like a car, but at racing speeds lateral load transfer pushes weight onto the outer wheels and risks tipping. Unlike a car, the legs can actively shift the body. This work uses a high-level model predictive controller to race the robot along a minimum-time raceline while commanding body roll to counteract load transfer.

**Key results:**
- High-level active-roll-control MPC built on a dynamic-bicycle model that outputs longitudinal acceleration, yaw moment, and roll moment commands `[a_x, M_ψ, M_θ]`.
- Offline minimum-time raceline optimization feeding the online MPC.
- Validated in closed-loop simulation and on Unitree Go2W hardware.

**Code:**
The [GitHub repository](https://github.com/meisman-ucb/go2w-roll-control-mpc) contains the MPC from the paper, the raceline generator, and a closed-loop simulation on the dynamic-bicycle model (Python, IPOPT). It also links videos of the hardware experiments.

Related: [RACER, learned residual dynamics for MPPI racing]({{ '/racer/' | relative_url }}) · [perception-driven roll control on 3D terrain]({{ '/nonplanar-terrain/' | relative_url }})
