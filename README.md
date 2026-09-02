# Autonomous Mobile Robot Navigation System

A Python-based robotics project developing an **Autonomous Mobile Robot (AMR) Navigation System** capable of understanding, planning, and navigating through previously unknown environments.

The project begins with a controlled **grid-based warehouse simulator** to establish the foundations of autonomous navigation and path planning. It progressively develops toward increasingly realistic robot simulation, sensing, localization, mapping, SLAM, dynamic obstacle avoidance, and eventually deployment on physical robotic hardware.

The warehouse simulator is therefore **not the final objective**. It is the controlled environment in which the navigation system is being developed and tested before moving toward real-world autonomous robotics.

---

# Final Objective

The long-term objective is to build an autonomous mobile robot capable of:

* Perceiving its surrounding environment through sensors
* Localizing itself within that environment
* Building and updating a map in real time
* Planning routes to a destination
* Navigating through previously unknown environments
* Detecting and avoiding obstacles
* Replanning when the environment changes
* Controlling its physical movement
* Operating autonomously with minimal human intervention

The system is intended to progress from **simulation to physical hardware**.

The final system can be represented as:

```text
             UNKNOWN ENVIRONMENT
                     ↓
                  SENSORS
                     ↓
                PERCEPTION
                     ↓
          ┌──────────┴──────────┐
          ↓                     ↓
      LOCALIZATION           MAPPING
          │                     │
          └──────────┬──────────┘
                     ↓
                PATH PLANNING
                     ↓
               MOTION CONTROL
                     ↓
               PHYSICAL ROBOT
                     ↓
                  SENSORS
                     ↺
```

The robot should continuously sense its surroundings, estimate its position, update its understanding of the environment, plan its movement, and execute that movement.

---

# Project Evolution

```text
V1
Basic Grid-Based Robot
        ↓
V2
Dynamic Environment + OOP
        ↓
V3
Autonomous Path Planning
        ↓
V4
Path Planning Engine
        ↓
V5
Advanced Dynamic Simulation
        ↓
V6
Realistic 2D Robot Simulation
        ↓
V7
Robot Physics + Sensor Simulation
        ↓
V8
Physical Robot Platform
        ↓
V9
Sensors + Reactive Obstacle Avoidance
        ↓
V10
Robot Localization
        ↓
V11
Real-Time Mapping
        ↓
V12
SLAM
        ↓
V13
Unknown-Environment Navigation
        ↓
V14
Dynamic Autonomous Navigation
        ↓
V15
Robust Physical Robot
        ↓
V16
General Autonomous Navigation
```

Each version adds another layer of capability rather than replacing the previous work.

---

# V3 — Autonomous Path Planning

V3 is the current completed milestone.

The simulator now supports:

* Dynamic irregular warehouse generation
* Random obstacles
* Multiple difficulty levels
* Weighted terrain
* Manual robot control
* Autonomous navigation
* BFS
* Dijkstra's algorithm
* A* search
* Algorithm comparison
* Path visualization
* Path-cost calculation
* Cells-explored measurement
* Solvable-map generation
* Real-time autonomous movement

V3 establishes the **path-planning foundation** of the larger autonomous navigation system.

---

# V3 Features

## Dynamic Environment Generation

Every simulation generates a new environment.

Current generation includes:

* Random warehouse width: **40–60 cells**
* Random warehouse height: **25–40 cells**
* Irregular polygon-based warehouse shapes
* Automatically generated boundaries
* Dynamically generated walkable areas
* Random robot starting position
* Automatically selected goal position
* Random obstacle placement
* Automatic regeneration until a solvable environment is produced

The environment is therefore no longer restricted to a simple rectangular grid.

---

# Difficulty System

Three difficulty levels control obstacle density:

| Difficulty | Obstacle Density |
| ---------- | ---------------: |
| Easy       |              10% |
| Medium     |              20% |
| Hard       |              30% |

The simulator verifies that a valid route exists before allowing the generated environment to proceed.

---

# Terrain System

V3 introduces **weighted terrain**.

Different cells have different movement costs:

| Terrain    | Symbol | Cost |
| ---------- | ------ | ---: |
| Normal     | `.`    |    1 |
| Rough      | `~`    |    3 |
| Very Rough | `^`    |    5 |

This creates a distinction between:

**Shortest path**

and

**Lowest-cost path**

Dijkstra and A* can therefore select a route based on movement cost rather than simply the number of cells travelled.

---

# Path-Planning Algorithms

V3 implements three path-planning algorithms.

## 1. Breadth-First Search — BFS

BFS explores the environment level-by-level using a queue.

It is used for:

* Path finding
* Solvability checking
* Shortest path in terms of number of moves
* Algorithm comparison

BFS does not account for terrain costs.

---

## 2. Dijkstra's Algorithm

Dijkstra's algorithm considers the movement cost associated with each terrain cell.

It searches for the **lowest-cost path** rather than simply the path containing the fewest moves.

This allows the robot to choose a longer route if doing so avoids expensive terrain.

---

## 3. A* Search

A* combines:

* Actual movement cost
* A heuristic estimating the remaining distance to the goal

The current implementation uses **Manhattan distance** as its heuristic.

A* is designed to reduce unnecessary exploration while still finding a cost-effective path.

---

# Autonomous Navigation

In Autonomous Mode:

```text
Environment Generation
        ↓
Obstacle + Terrain Generation
        ↓
Path Planning
        ↓
Path Calculation
        ↓
Path Visualization
        ↓
Autonomous Robot Movement
        ↓
Goal
```

The selected algorithm calculates a route and the robot automatically follows it.

Supported algorithms:

```text
BFS
Dijkstra
A*
```

This is the first stage in developing autonomous navigation.

At this stage, the environment is still known to the robot. Future versions will progressively remove that assumption.

---

# Manual Navigation

V3 retains manual control.

Controls:

```text
W / ↑  → Up
A / ←  → Left
S / ↓  → Down
D / →  → Right
Q      → Quit
```

Manual mode does not use path planning to control the robot.

BFS may be used beforehand to verify that the generated environment contains a valid route.

This provides a direct comparison between:

* Human-controlled navigation
* Algorithm-controlled navigation

---

# Algorithm Comparison

V3 includes a dedicated comparison mode.

All three algorithms are evaluated on the **same environment**, with the same:

* Robot position
* Goal
* Obstacles
* Terrain

The simulator measures:

* Path length
* Total path cost
* Cells explored

Example:

```text
BFS
Path length: ...
Total cost: ...
Cells explored: ...

Dijkstra
Path length: ...
Total cost: ...
Cells explored: ...

A*
Path length: ...
Total cost: ...
Cells explored: ...
```

The calculated paths are also displayed directly within the environment.

This allows the algorithms to be compared experimentally rather than only theoretically.

---

# Path Visualization

The terminal visualization represents the environment using:

```text
R  → Robot
G  → Goal
█  → Boundary / obstacle
.  → Normal terrain
~  → Rough terrain
^  → Very rough terrain
*  → Calculated path
```

During autonomous navigation, the robot follows the calculated path while the environment updates in real time.

---

# V3 Architecture

The simulator is structured around several major components.

## `Warehouse`

Responsible for the environment:

* Width
* Height
* Obstacles
* Goal position
* Boundary cells
* Walkable cells
* Terrain costs

## `Robot`

Responsible for robot state and movement:

```text
move_up()
move_down()
move_left()
move_right()
```

## Path Planning

```text
bfs()
dijkstra()
a_star()
find_path()
```

## Environment Generation

```text
generate_warehouse_shape()
generate_terrain()
generate_obstacles()
```

## Visualization

```text
display_warehouse()
display_header()
```

This separation provides a foundation for replacing the current simplified grid representation with increasingly realistic simulation and robotics components.

---

# V1 — Foundation

V1 established the basic grid-based environment.

It introduced:

* Fixed 35 × 15 warehouse
* Robot movement
* Goal
* Obstacles
* Boundary collision
* Win/Lose conditions
* Move counter
* Terminal visualization
* Basic BFS solvability checking

V1 established the fundamental environment and movement model.

---

# V2 — Dynamic Environment + OOP

V2 transformed the fixed simulator into a dynamic system.

It introduced:

* Random warehouse dimensions
* Random robot starting position
* Random goal
* Difficulty levels
* Random obstacle generation
* WASD controls
* Arrow-key controls
* Replay functionality
* Improved terminal interface
* Object-Oriented Programming
* `Warehouse` and `Robot` classes
* Solvable-map generation

V2 established the software architecture required for V3.

---

# Future Development

The project will progressively move from **known-map path planning** toward **autonomous navigation in unknown environments**.

## V4 — Path Planning Engine

Planned work:

* Formalize BFS, Dijkstra and A* into a dedicated planning layer
* Benchmark algorithms
* Compare computational efficiency
* Compare path quality
* Improve planner architecture
* Expand weighted navigation

---

## V5 — Advanced Dynamic Simulation

Planned work:

* Dynamic obstacles
* Restricted areas
* Multiple obstacle types
* More complex environments
* Changing goals
* Larger environments
* Path replanning

---

## V6 — Realistic 2D Simulation

The simulation will progress beyond a terminal grid toward a more realistic 2D robot environment.

Planned concepts:

* Continuous coordinates
* Robot orientation
* Robot dimensions
* Movement constraints
* Collision geometry
* Simulation state
* Sensor simulation

The objective is to make the simulated robot behave more like an actual mobile robot.

---

## V7 — Robot Physics + Sensor Simulation

The robot model will begin incorporating realistic physical behavior.

Potential components include:

* Velocity
* Acceleration
* Turning
* Wheel movement
* Sensor measurements
* Sensor noise
* Collision physics
* Robot dynamics

The software architecture will increasingly resemble a real robotics system.

---

## V8 — Physical Robot Platform

The navigation system will begin transitioning from simulation to hardware.

Initial platform:

```text
ESP32
  ↓
Motor Driver
  ↓
DC Motors
  ↓
Robot Chassis
  ↓
Battery
```

The first objective is reliable low-level robot control.

The robot must be able to:

* Move forward
* Move backward
* Turn
* Stop
* Receive commands
* Communicate with the navigation software

---

## V9 — Sensors + Reactive Obstacle Avoidance

Sensors will provide the robot with information about its immediate surroundings.

The system will introduce:

* Distance sensors
* Obstacle detection
* Emergency stopping
* Reactive obstacle avoidance

The robot will begin responding to obstacles that were not explicitly provided in advance.

---

## V10 — Localization

The robot must determine:

> **Where am I?**

The system will introduce concepts such as:

* Coordinate frames
* Robot pose
* Odometry
* Wheel encoders
* Position estimation
* Orientation estimation
* Sensor uncertainty
* Sensor fusion

The robot's pose can be represented as:

```text
x
y
θ
```

representing position and orientation.

---

## V11 — Real-Time Mapping

The robot must determine:

> **What does my environment look like?**

The system will progressively build maps from sensor observations.

A potential representation is an:

**Occupancy Grid Map**

Instead of receiving a complete map beforehand, the robot will construct its understanding of the environment while moving.

---

## V12 — SLAM

SLAM introduces the combined problem of:

**Simultaneous Localization and Mapping**

The robot must simultaneously:

* Estimate its position
* Build a map
* Update that map as it moves
* Correct localization errors
* Continue navigating

Conceptually:

```text
Move
 ↓
Sense
 ↓
Estimate Position
 ↓
Update Map
 ↓
Move
 ↓
Sense
 ↓
Correct Estimate
 ↓
Update Map
 ↺
```

---

## V13 — Unknown-Environment Navigation

The system will combine:

* Perception
* Localization
* Mapping
* Path planning
* Motion control

The robot will enter environments it has not previously been given a complete map of.

The navigation loop becomes:

```text
Sense
 ↓
Understand Environment
 ↓
Localize
 ↓
Update Map
 ↓
Plan
 ↓
Move
 ↓
Sense Again
 ↺
```

This represents the transition from **path planning on known maps** to **autonomous navigation**.

---

## V14 — Dynamic Autonomous Navigation

The robot must handle environments that change while it is operating.

Potential scenarios:

* Moving obstacles
* People
* Newly detected objects
* Blocked routes
* Temporary obstacles
* Sensor noise
* Localization errors

The system should be capable of:

```text
Detect Change
      ↓
Update Environment Model
      ↓
Recalculate Route
      ↓
Continue Navigation
```

---

## V15 — Robust Physical Robot

Simulation results must eventually survive real-world conditions.

The system will address:

* Sensor noise
* Wheel slip
* Motor inconsistencies
* Battery variation
* Communication latency
* Measurement errors
* Computational limitations
* Hardware failures
* Physical constraints

The objective is to close the gap between simulated and physical navigation.

---

## V16 — General Autonomous Navigation

The final development direction is to move beyond a system designed specifically around one warehouse layout.

The architecture should be capable of operating across supported unfamiliar environments such as:

```text
Warehouse
Office
Laboratory
Classroom
Hallway
Other Indoor Environments
```

The objective is not to create a separate navigation system for every environment.

The objective is to develop a **general autonomous navigation architecture** that can perceive, map, localize, plan, and navigate within previously unknown environments under its supported operating conditions.

---

# Core Robotics Architecture

The eventual system will consist of several interacting subsystems:

```text
                 AUTONOMOUS ROBOT
                        │
        ┌───────────────┼───────────────┐
        ↓               ↓               ↓
    PERCEPTION      LOCALIZATION      MAPPING
        │               │               │
        └───────────────┼───────────────┘
                        ↓
                  PATH PLANNING
                        ↓
                 MOTION PLANNING
                        ↓
                  MOTOR CONTROL
                        ↓
                      ROBOT
                        ↓
                    SENSORS
                        ↺
```

Path planning is therefore only **one component** of the final system.

The project progressively develops each component and eventually integrates them into one autonomous navigation system.

---

# Technologies

Current technologies:

* **Python**
* Object-Oriented Programming
* `random`
* `math`
* `heapq`
* `collections.deque`
* `msvcrt`
* `os`
* `time`
* ANSI terminal escape codes

Current algorithms:

* Breadth-First Search
* Dijkstra's Algorithm
* A* Search
* Polygon-based point-in-polygon testing
* Weighted path-cost calculation

Future technologies and concepts may include:

* Robotics simulation
* Robot physics
* Sensors
* Embedded systems
* Localization
* Mapping
* SLAM
* Motion planning
* Control systems
* ROS 2
* Computer vision
* Sensor fusion

Technologies will be introduced when they become necessary to the architecture rather than being added simply for complexity.

---

# Project Philosophy

The project follows a progression from **controlled problems to increasingly realistic autonomous systems**.

```text
Known Environment
       ↓
Known Map
       ↓
Path Planning
       ↓
Dynamic Environment
       ↓
Realistic Simulation
       ↓
Sensors
       ↓
Localization
       ↓
Mapping
       ↓
SLAM
       ↓
Unknown Environment
       ↓
Physical Robot
       ↓
Autonomous Navigation
```

The objective is to understand and implement the underlying systems rather than simply assemble a collection of robotics libraries.

---

# Current Milestone

## V3 — COMPLETE

Current capabilities:

* Dynamic irregular environments
* Random obstacles
* Difficulty levels
* Weighted terrain
* Manual control
* Autonomous navigation
* BFS
* Dijkstra
* A*
* Algorithm comparison
* Path visualization
* Path-cost calculation
* Cells-explored measurement
* Solvable-map generation
* Real-time autonomous movement

The V3 implementation has been debugged and integrated into the repository's `main` branch.

### Current Position

```text
V1 → V2 → V3 → V4 → V5 → ... → V16
             ↑
           HERE
```

The current system solves a **controlled path-planning problem**.

The next major objective is to progressively remove the assumptions that the environment, map, and robot state are already known.

---

# Repository Structure

```text
warehouse-robot-simulator/
│
├── warehouse_robot_simulator.py
├── README.md
├── LICENSE
├── .gitignore
│
└── images/
    ├── game_start.png
    ├── middle_game.png
    └── texture.png
```

The repository structure will evolve as the simulator develops into a larger robotics system.

---

# Learning Outcomes

Through V1–V3, the project has developed practical experience with:

* Python programming
* Functions
* Classes and objects
* Object-Oriented Programming
* Lists, tuples, sets and dictionaries
* Coordinate systems
* Grid-based environments
* Collision detection
* Randomized environment generation
* Procedural geometry
* Terminal input handling
* Terminal visualization
* Queue-based search
* Priority queues
* Graph traversal
* Shortest-path algorithms
* Weighted path planning
* Heuristics
* Path reconstruction
* Algorithm comparison
* Simulation state management

Future versions will extend these foundations into:

* Robotics
* Simulation
* Sensor processing
* Localization
* Mapping
* SLAM
* Motion planning
* Control systems
* Embedded robotics
* Autonomous navigation

---

# Final Vision

This project is evolving from a simple question:

> **"What is the best path from A to B?"**

toward a much larger question:

> **"How can a robot enter an unfamiliar environment, understand where it is, build a representation of its surroundings, determine where it needs to go, plan a safe route, and autonomously get there?"**

The warehouse simulator is the first controlled environment in which that problem is being explored.

The ultimate objective is a **physical Autonomous Mobile Robot capable of real-time perception, localization, mapping, planning, obstacle avoidance, and autonomous navigation in previously unknown environments.**

---

# Author

**V. Akshaj Ram Charan**
