# Warehouse Robot Simulator

A Python-based terminal warehouse navigation simulator developed as the software foundation for a larger **warehouse robotics project**.

The project evolves from basic grid-based robot movement into **dynamic warehouse generation, weighted terrain, autonomous path planning, algorithm comparison, and manual robot control**.

The long-term objective is to progress from a software simulation to a **physical autonomous warehouse robot**.

---

## Project Evolution

```text
V1
Basic Warehouse Simulator
        ↓
V2
Dynamic Warehouse + OOP
        ↓
V3
Path Planning + Autonomous Navigation
        ↓
V4
Advanced Simulation
        ↓
V5
Robotics / Physical Robot Preparation
        ↓
ESP32 Physical Robot
        ↓
Real-World Warehouse Navigation
```

---

# V3 — Autonomous Warehouse Navigation

V3 is the major path-planning milestone of the project.

The simulator now supports **three different path-planning algorithms**, weighted terrain, irregular warehouse shapes, autonomous navigation, algorithm comparison, and manual robot control.

Instead of simply moving a robot around a fixed grid, V3 allows the robot to **calculate and follow a route through a dynamically generated warehouse**.

---

## V3 Features

### Dynamic Warehouse Generation

Every game generates a new warehouse.

* Random warehouse width: **40–60 cells**
* Random warehouse height: **25–40 cells**
* Irregular polygon-based warehouse shapes
* Automatically generated warehouse boundaries
* Dynamically generated walkable areas
* Random robot starting position
* Automatically selected goal position
* Random obstacle placement
* Automatic regeneration until a solvable map is produced

The warehouse is no longer restricted to a simple rectangular layout.

---

## Difficulty System

Three difficulty levels control obstacle density:

| Difficulty | Obstacle Density |
| ---------- | ---------------: |
| Easy       |              10% |
| Medium     |              20% |
| Hard       |              30% |

The simulator checks whether the generated warehouse is navigable before allowing the game to proceed.

---

# Terrain System

V3 introduces **weighted terrain**.

Different floor cells have different movement costs:

| Terrain    | Symbol | Cost |
| ---------- | ------ | ---: |
| Normal     | `.`    |    1 |
| Rough      | `~`    |    3 |
| Very Rough | `^`    |    5 |

Terrain is randomly generated across the warehouse.

This creates an important distinction between:

**shortest path**

and

**lowest-cost path**.

Dijkstra and A* can therefore consider terrain cost when selecting a route.

---

# Path-Planning Algorithms

V3 implements three path-planning algorithms from scratch.

## 1. Breadth-First Search — BFS

BFS explores the warehouse level-by-level using a queue.

It is used for:

* Path finding
* Solvability checking
* Shortest path in terms of number of moves
* Comparing algorithm performance

BFS does not consider terrain costs.

---

## 2. Dijkstra's Algorithm

Dijkstra's algorithm considers the movement cost of each terrain cell.

It searches for the **lowest-cost path**, rather than simply the path containing the fewest moves.

This allows the robot to choose a slightly longer route if that route avoids expensive terrain.

---

## 3. A* Search

A* combines:

* Actual movement cost
* A heuristic estimating the remaining distance to the goal

The implementation uses Manhattan distance as its heuristic.

A* is designed to reach the goal more efficiently than uninformed search while still considering terrain costs.

---

# Autonomous Mode

In Autonomous Mode:

1. A warehouse is generated.
2. Obstacles and terrain are generated.
3. The selected algorithm calculates a route.
4. The route is displayed on the warehouse.
5. The robot automatically follows the calculated path.
6. The simulator displays the robot's movement step-by-step.
7. The robot reaches the goal automatically.

Supported algorithms:

```text
BFS
Dijkstra
A*
```

The robot is therefore no longer dependent on manual keyboard input to navigate to the goal.

---

# Manual Mode

V3 also retains manual control.

The robot can be controlled using:

```text
W / ↑  → Up
A / ←  → Left
S / ↓  → Down
D / →  → Right
Q      → Quit
```

Manual mode does **not** use path finding to control the robot.

BFS is only used beforehand to verify that the generated warehouse has a valid route to the goal.

This separates:

* **Human-controlled navigation**
* **Algorithm-controlled navigation**

which is useful for comparing manual and autonomous robot behaviour.

---

# Algorithm Comparison Mode

V3 includes a dedicated comparison mode.

All three algorithms are executed on the **same warehouse, with the same robot position, goal, obstacles, and terrain**.

The simulator reports:

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

The calculated paths are also displayed directly on the warehouse.

Different colours are used to distinguish the algorithms and shared sections of their routes.

---

# Path Visualization

The terminal visualization shows:

```text
R  → Robot
G  → Goal
█  → Boundary / obstacle
.  → Normal terrain
~  → Rough terrain
^  → Very rough terrain
*  → Calculated path
```

During autonomous navigation, the robot moves through the calculated path while the terminal updates in real time.

---

# V3 Architecture

The simulator is structured around several major components.

### `Warehouse`

Stores the warehouse environment:

* Width
* Height
* Obstacles
* Goal position
* Boundary cells
* Walkable cells
* Terrain costs

### `Robot`

Stores the robot's position and provides movement operations:

```text
move_up()
move_down()
move_left()
move_right()
```

### Path-planning functions

```text
bfs()
dijkstra()
a_star()
find_path()
```

### Environment generation

```text
generate_warehouse_shape()
generate_terrain()
generate_obstacles()
```

### Visualization

```text
display_warehouse()
display_header()
```

This separation makes the simulator easier to extend toward future robotics applications.

---

# V1 — Foundation

V1 established the basic warehouse simulation.

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

V1 was the foundation for everything that followed.

---

# V2 — Dynamic Warehouse + OOP

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

V2 established the architecture that allowed V3 to focus on navigation algorithms.

---

# Technologies

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

### Algorithms

* Breadth-First Search
* Dijkstra's Algorithm
* A* Search
* Polygon-based point-in-polygon testing
* Weighted path-cost calculation

---

# How to Run

Clone the repository or download the project.

Open a terminal inside the project directory and run:

```bash
python warehouse_robot_simulator.py
```

The simulator will generate a warehouse and guide you through:

```text
Difficulty
    ↓
Mode
    ↓
Algorithm (Autonomous Mode)
    ↓
Warehouse Navigation
```

---

# Project Structure

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

---

# Learning Outcomes

Through V1–V3, the project developed practical experience with:

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

---

# Project Direction

The purpose of this project is not to remain a terminal game.

The simulator is being developed as a progression toward robotics:

```text
Python
   ↓
Warehouse Simulation
   ↓
Path Planning Algorithms
   ↓
Autonomous Navigation
   ↓
Advanced Robot Simulation
   ↓
Robotics Concepts
   ↓
ESP32
   ↓
Physical Robot
   ↓
Sensors
   ↓
Real-World Path Planning
   ↓
Warehouse Navigation
```

The eventual objective is a physical robot capable of receiving a destination, planning a route, navigating through an environment, avoiding obstacles, and operating autonomously.

---

# Current Milestone

## V3 — COMPLETE

V3 currently includes:

* Dynamic irregular warehouses
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

---

# Author

**V. Akshaj Ram Charan**

This repository documents the development of a warehouse robotics project from a basic Python grid simulator toward autonomous navigation and eventually a physical warehouse robot.
