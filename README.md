# Warehouse Robot Simulator

A Python terminal-based warehouse navigation simulator built as the first milestone of a larger warehouse robotics project.

The project is being developed incrementally, starting with a simple manually controlled warehouse and gradually moving toward autonomous warehouse navigation and eventually a physical warehouse robot.

---

## V1 — Foundation

The first version established the core warehouse simulation.

### Features

* Fixed **35 × 15** warehouse
* Robot (`R`) with manual movement
* Randomly generated goal (`G`)
* Warehouse boundary walls
* Random obstacle generation
* Collision detection
* Win/Lose conditions
* Move counter
* Colored terminal visualization
* Automatic map regeneration
* **Breadth-First Search (BFS)** to guarantee that the generated map is solvable
* Quit option

V1 focused on building the fundamental grid, movement, collision, and path-validity systems.

---

## V2 — Dynamic Warehouse Simulator

V2 builds directly on V1 and introduces a more dynamic and replayable simulation.

### Added Features

* **Random warehouse dimensions**

  * Width: 20–40
  * Height: 10–20
* **Random robot starting position**
* **Random goal position**
* **Difficulty levels**

  * Easy — 10% obstacle density
  * Medium — 20% obstacle density
  * Hard — 30% obstacle density
* Solvable map generation maintained using BFS
* **W / A / S / D controls**
* **Arrow-key controls**
* Improved game-start information

  * Difficulty
  * Warehouse dimensions
  * Map-generation attempts
  * Controls
* Move counter
* Replay / Play Again functionality
* Clean terminal reset between games
* Object-Oriented Programming introduced through the `Warehouse` and `Robot` classes

V2 turns the original fixed demonstration into a configurable and replayable warehouse simulator.

---

## Controls

| Key       | Action     |
| --------- | ---------- |
| `W` / `↑` | Move Up    |
| `A` / `←` | Move Left  |
| `S` / `↓` | Move Down  |
| `D` / `→` | Move Right |
| `Q`       | Quit       |

---

## Symbols

| Symbol | Meaning                    |
| ------ | -------------------------- |
| `R`    | Robot                      |
| `G`    | Goal                       |
| `X`    | Robot has reached the goal |
| `█`    | Warehouse boundary         |
| `█`    | Obstacle                   |
| `.`    | Empty space                |

The terminal uses colors to distinguish the robot, goal, boundaries, and obstacles.

---

## Algorithms Used

### Breadth-First Search (BFS)

BFS is used to check whether a generated warehouse contains a valid path from the robot to the goal.

If the generated map is unsolvable, the simulator discards it and generates another map until a valid route is found.

This ensures that every generated game is winnable.

---

## Technologies

* **Python**
* `random` — random warehouse, robot, goal, and obstacle generation
* `os` — terminal clearing
* `msvcrt` — keyboard input and arrow-key controls
* ANSI escape codes — terminal colors
* **Object-Oriented Programming (OOP)**
* **Breadth-First Search (BFS)**

---

## How to Run

Clone the repository or download the project files.

Open a terminal in the project directory and run:

```bash
python warehouse_robot_simulator.py
```

The simulator will generate a warehouse and ask you to select a difficulty.

---

## Project Structure

```text
warehouse2D_game1/
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

## Learning Outcomes

This project developed practical understanding of:

* Python fundamentals
* Functions
* Classes and objects
* Object-Oriented Programming
* Lists, tuples, and sets
* Coordinate systems
* Grid-based movement
* Collision detection
* Random generation
* Terminal input handling
* Terminal visualization
* BFS and queue-based algorithms
* Path validation
* Procedural map generation
* Game-state management

---

## Project Direction

This simulator is the first stage of a larger warehouse robotics project.

The planned progression is:

```text
Python Fundamentals
        ↓
Warehouse Robot Simulator
        ↓
BFS
        ↓
Dijkstra
        ↓
A*
        ↓
Advanced Visualization
        ↓
GUI Simulator
        ↓
Robot Simulation
        ↓
ESP32 Physical Robot
        ↓
Real-World Warehouse Navigation
```

The long-term objective is to progress from a manually controlled grid simulator to an autonomous robot capable of performing path planning and navigation in a warehouse environment.

---

## Project Evolution

### V1

A fixed warehouse demonstrating the fundamentals of grid-based robot navigation.

### V2

A dynamic warehouse with random dimensions, random starting conditions, difficulty levels, multiple control methods, OOP, solvable-map generation, and replayability.

### Future Versions

The focus will shift from manually controlling the robot toward **algorithmic path planning and autonomous navigation**.

---

## Author

**V. Akshaj Ram Charan**

This repository documents the development of a warehouse robotics project from a basic Python grid simulator toward autonomous navigation and eventually a physical warehouse robot.
