# Awesome Humanoid Ball Sports [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

As robot learning leans more and more toward scaling, it can seem like there is less and less left for academic labs to do. I've long believed that humanoid sports is a topic especially well suited to academia: it doesn't need huge amounts of compute or data, but it does take a lot of effort and ingenuity. I made this list to make literature review in this area easier for everyone.

It collects research on humanoid robots playing **table tennis, tennis, badminton, soccer and basketball**, plus a map of which groups work on which sport.

<!-- gen:stats -->
**41** works · **32** groups · **27** institutions
<!-- /gen -->

Each entry lists when it first appeared, where it was published (📣 = public demo, no paper yet), which robot it uses, whether it was shown on real hardware (✅ real robot, 🖥️ simulation only), and links to its project page and code.

> [!NOTE]
> The tables and the map are generated from [`data/papers.toml`](data/papers.toml) and [`data/labs.toml`](data/labs.toml). To add or fix an entry, edit those files; see [CONTRIBUTING.md](CONTRIBUTING.md).

## Contents

- [🌍 Who's Working on What](#-whos-working-on-what)
- [🏓 Table Tennis](#-table-tennis)
- [🎾 Tennis](#-tennis)
- [🏸 Badminton](#-badminton)
- [⚽ Soccer](#-soccer)
- [🏀 Basketball](#-basketball)

## 🌍 Who's Working on What

Click a marker to see an institution's groups (named by each paper's last author), the sports they work on, and their papers.

<!-- gen:map -->
```geojson
{"type": "FeatureCollection", "features": [
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-118.1253, 34.1377]}, "properties": {"Institution": "Caltech", "Sports": "🎾 Tennis", "AMBER Lab — Aaron D. Ames": "TaskNPoint (2026.06)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-79.9428, 40.4439]}, "properties": {"Institution": "Carnegie Mellon University", "Sports": "⚽ Soccer", "Safe AI Lab — Ding Zhao": "Banana Kick (2026.09) · Robotic Penalty Kicks (2026.09)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-76.4735, 42.4534]}, "properties": {"Institution": "Cornell University", "Sports": "⚽ Soccer", "Qi Wu": "Dribble Master (2025.05)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [116.314, 39.9835]}, "properties": {"Institution": "DeepCybo", "Sports": "🎾 Tennis · 🏸 Badminton", "Kai Chen": "CyboRacket (2026.03)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [8.5477, 47.3763]}, "properties": {"Institution": "ETH Zurich", "Sports": "🏸 Badminton", "Robotic Systems Lab — Marco Hutter": "Humanoid badminton (teaser) (2026.09)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-0.126, 51.5333]}, "properties": {"Institution": "Google DeepMind", "Sports": "⚽ Soccer", "Nicolas Heess": "Agile Soccer Skills (OP3) (2023.04) · Soccer from Egocentric Vision (2024.05)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [114.1371, 22.283]}, "properties": {"Institution": "HKU", "Sports": "🏓 Table Tennis · 🏸 Badminton · ⚽ Soccer", "ArcLab — Peng Lu": "STOFT (2025.10) · LHBS (2026.02)", "MMLab — Ping Luo": "SMASH (2026.04) · SMASH 2.0 (2026.09)", "OpenDriveLab — Hongyang Li": "RoboNaldo (2026.06)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [114.2655, 22.3364]}, "properties": {"Institution": "HKUST", "Sports": "⚽ Soccer · 🏀 Basketball", "Ping Tan": "HumanX (2026.02)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-71.0942, 42.3601]}, "properties": {"Institution": "MIT", "Sports": "⚽ Soccer", "Improbable AI Lab — Pulkit Agrawal": "Joga (2026.09)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [116.298, 39.959]}, "properties": {"Institution": "Noetix Robotics", "Sports": "⚽ Soccer", "Xiaoyu Tian": "SkillX (2026.09)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [116.4074, 39.9042]}, "properties": {"Institution": "Phybot", "Sports": "🏸 Badminton", "Xiaoyu Ren": "Humanoid Whole-Body Badminton (2025.11)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-86.9212, 40.4237]}, "properties": {"Institution": "Purdue University", "Sports": "🏓 Table Tennis", "TRACE Lab — Yan Gu": "PACE (2025.09)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [12.5144, 41.9031]}, "properties": {"Institution": "Sapienza University of Rome", "Sports": "⚽ Soccer", "Lab RoCoCo — Daniele Nardi": "Multi Robot Coordination (2025.09)", "Lab RoCoCo — Luca Iocchi": "Vision-Based Dribbling (2026.07)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [121.46, 31.179]}, "properties": {"Institution": "Shanghai AI Lab", "Sports": "🎾 Tennis · ⚽ Soccer", "Jiangmiao Pang": "Humanoid Goalkeeper (2025.10) · AdaPT (2026.08)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [121.4337, 31.0252]}, "properties": {"Institution": "Shanghai Jiao Tong University", "Sports": "⚽ Soccer", "Yue Gao": "HierKick (2026.03)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-79.928, 40.46]}, "properties": {"Institution": "Skild AI", "Sports": "⚽ Soccer", "—": "Physical Self-Play (2026.09)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [121.437, 31.188]}, "properties": {"Institution": "TeleAI", "Sports": "⚽ Soccer", "Xuelong Li": "Learning Soccer Skills for Humanoid Robots (2026.02)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [116.321, 40.0023]}, "properties": {"Institution": "Tsinghua University", "Sports": "🎾 Tennis · ⚽ Soccer", "Li Yi": "LATENT (2026.03)", "Mingguo Zhao": "Vision-Driven Reactive Soccer (2025.11)", "Yiming Li": "DAVIS (2026.09)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-122.2585, 37.8719]}, "properties": {"Institution": "UC Berkeley", "Sports": "🏓 Table Tennis", "S. Shankar Sastry": "HITTER (2025.08)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-118.4469, 34.0709]}, "properties": {"Institution": "UCLA", "Sports": "⚽ Soccer", "RoMeLa — Dennis W. Hong": "MPC with Visibility Graphs (2025.04) · Model-Based Humanoid Soccer (2025.12)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-72.5284, 42.3893]}, "properties": {"Institution": "UMass Amherst", "Sports": "⚽ Soccer", "Donghyun Kim": "Biomechanics-Inspired Kicking (2024.07)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-118.2859, 34.0219]}, "properties": {"Institution": "USC", "Sports": "⚽ Soccer", "DRCL — Quan Nguyen": "Preferenced Oracle Guided Policies (2024.10)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-97.7339, 30.2851]}, "properties": {"Institution": "UT Austin", "Sports": "⚽ Soccer", "LARG — Peter Stone": "Agile Striker Skills (2025.12)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-89.4125, 43.0766]}, "properties": {"Institution": "UW–Madison", "Sports": "⚽ Soccer", "Josiah P. Hanna": "RL Within the Classical Stack (2024.12) · Multi-Robot Collaboration (2025.03)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-8.6598, 40.632]}, "properties": {"Institution": "University of Aveiro", "Sports": "⚽ Soccer", "IEETA — Nuno Lau": "Skill-Set-Primitives for RoboCup (2023.12)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [7.1024, 50.7339]}, "properties": {"Institution": "University of Bonn", "Sports": "⚽ Soccer", "Autonomous Intelligent Systems — Sven Behnke": "NimbRo (RoboCup 2023 winner) (2024.01) · Maximum Impulse Kicking (2024.12)"}},
{"type": "Feature", "geometry": {"type": "Point", "coordinates": [9.9847, 53.5667]}, "properties": {"Institution": "University of Hamburg", "Sports": "⚽ Soccer", "TAMS — Jianwei Zhang": "SoccerDiffusion (2025.04)"}}
]}
```
<!-- /gen -->


## 🏓 Table Tennis

<!-- gen:papers/table-tennis -->
| Date | Paper | Venue | Robot | Real | Group | Links |
|---|---|---|---|---|---|---|
| 2025.08 | [HITTER: A HumanoId Table TEnnis Robot via Hierarchical Planning and Learning](https://arxiv.org/abs/2508.21043) | ICRA 2026 | Unitree G1 | ✅ | S. Shankar Sastry, UC Berkeley | [project](https://humanoid-table-tennis.github.io/) |
| 2025.09 | [PACE: Physics Augmentation for Coordinated End-to-end Reinforcement Learning toward Versatile Humanoid Table Tennis](https://arxiv.org/abs/2509.21690) | ICRA 2026 | Booster T1 | ✅ | Yan Gu, Purdue University | [project](https://purdue-tracelab.github.io/ttrobot.github.io/) · [code](https://github.com/purdue-tracelab/PACE-ICRA2026) |
| 2026.04 | [SMASH: Mastering Scalable Whole-Body Skills for Humanoid Ping-Pong with Egocentric Vision](https://arxiv.org/abs/2604.01158) | arXiv | Unitree G1 | ✅ | Ping Luo, HKU | [project](https://mmlab.hk/Smash/) |
| 2026.09 | [SMASH 2.0 (demo video)](https://www.xiaohongshu.com/discovery/item/6ab5a0a1000000000200f1c0) | 📣 Announced | Unitree G1 | ✅ | Ping Luo, HKU | — |
<!-- /gen -->

## 🎾 Tennis

<!-- gen:papers/tennis -->
| Date | Paper | Venue | Robot | Real | Group | Links |
|---|---|---|---|---|---|---|
| 2026.03 | [CyboRacket: A Perception-to-Action Framework for Humanoid Racket Sports](https://arxiv.org/abs/2603.14605) | arXiv | Unitree G1 | ✅ | Kai Chen, DeepCybo | — |
| 2026.03 | [Learning Athletic Humanoid Tennis Skills from Imperfect Human Motion Data](https://arxiv.org/abs/2603.12686) | arXiv | Unitree G1 | ✅ | Li Yi, Tsinghua University | [project](https://zzk273.github.io/LATENT/) · [code](https://github.com/GalaxyGeneralRobotics/LATENT) |
| 2026.06 | [TaskNPoint: How to Teach Your Humanoid to Hit a Backhand in Minutes](https://arxiv.org/abs/2606.26215) | arXiv | Unitree G1 | ✅ | Aaron D. Ames, Caltech | [project](https://ilonadem.github.io/tasknpoint_website/) · [code](https://github.com/wernerb43/tasknpoint) |
| 2026.08 | [Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking](https://arxiv.org/abs/2608.20087) | CoRL 2026 | Unitree G1, Dobot Atom | ✅ | Jiangmiao Pang, Shanghai AI Lab | [project](https://humanoidtennis.github.io/AdaPT/) · [code](https://github.com/noitom-robotics/AdaPT) |
| 2026.09 | [ATHLETE: Learning Reactive Humanoid Tennis via Trajectory-Guided Motion Matching](https://hazintihoa.github.io/athlete.github.io/) | 📣 Announced | Unitree G1 | ✅ | — | code (soon) |
<!-- /gen -->

## 🏸 Badminton

<!-- gen:papers/badminton -->
| Date | Paper | Venue | Robot | Real | Group | Links |
|---|---|---|---|---|---|---|
| 2025.11 | [Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum](https://arxiv.org/abs/2511.11218) | arXiv | Phybot humanoid (1.28 m) | ✅ | Xiaoyu Ren, Phybot | [project](https://humanoid-badminton.github.io/Humanoid-Whole-Body-Badminton-via-Multi-Stage-Reinforcement-Learning/) |
| 2026.02 | [Learning Human-Like Badminton Skills for Humanoid Robots](https://arxiv.org/abs/2602.08370) | arXiv | EngineAI PM01 | ✅ | Peng Lu, HKU | [project](https://astrorix.github.io/LHBS/) |
| 2026.03 | [CyboRacket: A Perception-to-Action Framework for Humanoid Racket Sports](https://arxiv.org/abs/2603.14605) | arXiv | Unitree G1 | ✅ | Kai Chen, DeepCybo | — |
| 2026.09 | [ETH humanoid badminton teaser: "We put this on the hardware!!"](https://x.com/JayHe748646/status/2103195667342737485) | 📣 Announced | — | ✅ | Marco Hutter, ETH Zurich | — |
<!-- /gen -->

## ⚽ Soccer

<!-- gen:papers/soccer -->
| Date | Paper | Venue | Robot | Real | Group | Links |
|---|---|---|---|---|---|---|
| 2023.04 | [Learning Agile Soccer Skills for a Bipedal Robot with Deep Reinforcement Learning](https://arxiv.org/abs/2304.13653) | Science Robotics 2024 | Robotis OP3 | ✅ | Nicolas Heess, Google DeepMind | [project](https://sites.google.com/view/op3-soccer) |
| 2023.12 | [Designing a skilled soccer team for RoboCup: exploring skill-set-primitives through reinforcement learning](https://arxiv.org/abs/2312.14360) | Neural Computing and Applications 2025 | NAO (SimSpark) | 🖥️ | Nuno Lau, University of Aveiro | [code](https://github.com/m-abr/FCPCodebase) |
| 2024.01 | [RoboCup 2023 Humanoid AdultSize Winner NimbRo: NimbRoNet3 Visual Perception and Responsive Gait with Waveform In-walk Kicks](https://arxiv.org/abs/2401.05909) | RoboCup 2023 Symposium | NimbRo-OP2X | ✅ | Sven Behnke, University of Bonn | — |
| 2024.05 | [Learning Robot Soccer from Egocentric Vision with Deep Reinforcement Learning](https://arxiv.org/abs/2405.02425) | CoRL 2024 | Robotis OP3 | ✅ | Nicolas Heess, Google DeepMind | [project](https://sites.google.com/view/vision-soccer) |
| 2024.07 | [A Biomechanics-Inspired Approach to Soccer Kicking for Humanoid Robots](https://arxiv.org/abs/2407.14612) | arXiv | PresToe | 🖥️ | Donghyun Kim, UMass Amherst | — |
| 2024.10 | [Preferenced Oracle Guided Multi-mode Policies for Dynamic Bipedal Loco-Manipulation](https://arxiv.org/abs/2410.01030) | arXiv | HECTOR, Berkeley Humanoid, Unitree G1/H1 | 🖥️ | Quan Nguyen, USC | — |
| 2024.12 | [Maximum Impulse Approach to Soccer Kicking for Humanoid Robots](https://arxiv.org/abs/2412.01480) | arXiv | NimbRo-OP2X | ✅ | Sven Behnke, University of Bonn | — |
| 2024.12 | [Reinforcement Learning Within the Classical Robotics Stack: A Case Study in Robot Soccer](https://arxiv.org/abs/2412.09417) | ICRA 2025 | NAO | ✅ | Josiah P. Hanna, UW–Madison | — |
| 2025.03 | [Multi-Robot Collaboration through Reinforcement Learning and Abstract Simulation](https://arxiv.org/abs/2503.05092) | ICRA 2025 | NAO | ✅ | Josiah P. Hanna, UW–Madison | — |
| 2025.04 | [Model Predictive Control with Visibility Graphs for Humanoid Path Planning and Tracking Against Adversarial Opponents](https://arxiv.org/abs/2504.02184) | ICRA 2025 | ARTEMIS | ✅ | Dennis W. Hong, UCLA | — |
| 2025.04 | [SoccerDiffusion: Toward Learning End-to-End Humanoid Robot Soccer from Gameplay Recordings](https://arxiv.org/abs/2504.20808) | arXiv | Wolfgang-OP | ✅ | Jianwei Zhang, University of Hamburg | [project](https://bit-bots.github.io/SoccerDiffusion) · [code](https://github.com/bit-bots/SoccerDiffusion) |
| 2025.05 | [Dribble Master: Learning Agile Humanoid Dribbling through Legged Locomotion](https://arxiv.org/abs/2505.12679) | ICRA 2026 | Booster T1 | ✅ | Qi Wu, Cornell University | [project](https://zhuoheng0910.github.io/dribble-master/) · [code](https://github.com/Zhuoheng0910/DribbleMaster) |
| 2025.09 | [Multi Robot Coordination in Highly Dynamic Environments: Tackling Asymmetric Obstacles and Limited Communication](https://arxiv.org/abs/2509.08859) | IAS-19 2025 | NAO | ✅ | Daniele Nardi, Sapienza University of Rome | — |
| 2025.10 | [Humanoid Goalkeeper: Learning from Position Conditioned Task-Motion Constraints](https://arxiv.org/abs/2510.18002) | arXiv | Unitree G1 | ✅ | Jiangmiao Pang, Shanghai AI Lab | [project](https://humanoid-goalkeeper.github.io/Goalkeeper/) · [code](https://github.com/InternRobotics/Humanoid-Goalkeeper) |
| 2025.10 | [Like Playing a Video Game: Spatial-Temporal Optimization of Foot Trajectories for Controlled Football Kicking in Bipedal Robots](https://arxiv.org/abs/2510.01843) | IROS 2025 | PEARL biped | ✅ | Peng Lu, HKU | [project](https://arclab-hku.github.io/STOFT/) |
| 2025.11 | [Learning Vision-Driven Reactive Soccer Skills for Humanoid Robots](https://arxiv.org/abs/2511.03996) | Science Robotics 2026 | Booster T1 | ✅ | Mingguo Zhao, Tsinghua University | [project](https://humanoid-kick.github.io) · [code](https://zenodo.org/records/21620490) |
| 2025.12 | [A Hierarchical, Model-Based System for High-Performance Humanoid Soccer](https://arxiv.org/abs/2512.09431) | arXiv | ARTEMIS | ✅ | Dennis W. Hong, UCLA | — |
| 2025.12 | [Learning Agile Striker Skills for Humanoid Soccer Robots from Noisy Sensory Input](https://arxiv.org/abs/2512.06571) | ICRA 2026 | Booster T1 | ✅ | Peter Stone, UT Austin | [project](https://humanoidsoccer.github.io) · [code](https://github.com/Daffan/humanoid-soccer) |
| 2026.02 | [HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos](https://arxiv.org/abs/2602.02473) | arXiv | Unitree G1 | ✅ | Ping Tan, HKUST | [project](https://wyhuai.github.io/human-x/) · code (soon) |
| 2026.02 | [Learning Soccer Skills for Humanoid Robots: A Progressive Perception-Action Framework](https://arxiv.org/abs/2602.05310) | arXiv | Unitree G1 | ✅ | Xuelong Li, TeleAI | [project](https://soccer-humanoid.github.io/) · [code](https://github.com/TeleHuman/HumanoidSoccer) |
| 2026.03 | [HierKick: Hierarchical Reinforcement Learning for Vision-Guided Soccer Robot Control](https://arxiv.org/abs/2603.00948) | arXiv | Booster T1 | ✅ | Yue Gao, Shanghai Jiao Tong University | — |
| 2026.06 | [RoboNaldo: Accurate, Stable and Powerful Humanoid Soccer Shooting via Motion-Guided Curriculum Reinforcement Learning](https://arxiv.org/abs/2606.11092) | CoRL 2026 | Unitree G1 | ✅ | Hongyang Li, HKU | [project](https://opendrivelab.com/RoboNaldo) · [code](https://github.com/OpenDriveLab/RoboNaldo) |
| 2026.07 | [Vision-Based Dribbling for Humanoid Soccer via Privileged Representation Learning](https://arxiv.org/abs/2607.12702) | arXiv | Booster T1 | 🖥️ | Luca Iocchi, Sapienza University of Rome | [project](https://lab-rococo-sapienza.github.io/learning-to-dribble/) · code (soon) |
| 2026.09 | [Banana Kick: Response-Informed Skill Evolution for Humanoid Soccer](https://arxiv.org/abs/2609.27269) | arXiv | Unitree G1 | ✅ | Ding Zhao, Carnegie Mellon University | — |
| 2026.09 | [DAVIS: A Depth-Only End-to-End Active-Vision Framework for Humanoid Soccer Skills](https://arxiv.org/abs/2609.28175) | arXiv | Noetix E1 | ✅ | Yiming Li, Tsinghua University | [project](https://thusi-lab.github.io/DAVIS/) |
| 2026.09 | [Dynamics-Induced Commitment in Learning-Based Robotic Penalty Kicks](https://arxiv.org/abs/2609.21100) | arXiv | Unitree G1 (vs. Go2 keeper) | ✅ | Ding Zhao, Carnegie Mellon University | — |
| 2026.09 | [Joga: a full-stack humanoid soccer system with active vision](https://x.com/nolan_fey/status/2102664694704042152) | 📣 Announced | Unitree G1 + actuated neck | ✅ | Pulkit Agrawal, MIT | — |
| 2026.09 | [Physical Self-Play](https://www.skild.ai/blogs/physical-self-play) | Blog | Full-size humanoid | ✅ | Skild AI | — |
| 2026.09 | [SkillX: Unified Multi-Skill Policy Learning for Humanoid Soccer](https://arxiv.org/abs/2609.06718) | CoRL 2026 | Noetix E1 | ✅ | Xiaoyu Tian, Noetix Robotics | [project](https://yzc0731.github.io/SkillX/) |
<!-- /gen -->

## 🏀 Basketball

<!-- gen:papers/basketball -->
| Date | Paper | Venue | Robot | Real | Group | Links |
|---|---|---|---|---|---|---|
| 2026.02 | [HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos](https://arxiv.org/abs/2602.02473) | arXiv | Unitree G1 | ✅ | Ping Tan, HKUST | [project](https://wyhuai.github.io/human-x/) · code (soon) |
<!-- /gen -->

## Contributing

Pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).
