# Warehouse Robot Simulator

A Python terminal-based warehouse navigation simulator built as the first milestone of a larger warehouse robotics project.

The simulator generates a random warehouse layout with obstacles and guarantees that the goal is always reachable using Breadth-First Search (BFS). The player manually controls the robot and must reach the goal without colliding with obstacles or warehouse walls.

---

## Features

* Random obstacle placement
* Random goal generation
* Warehouse boundary walls
* Solvable map generation using BFS
* Manual robot movement (W, A, S, D)
* Collision detection
* Win/Lose conditions
* Colored terminal visualization
* Automatic map regeneration until a valid path exists

---

## Controls

| Key | Action     |
| --- | ---------- |
| W   | Move Up    |
| A   | Move Left  |
| S   | Move Down  |
| D   | Move Right |
| Q   | Quit Game  |

---

## Symbols

| Symbol     | Meaning            |
| ---------  | ------------------ |
| R          | Robot              |
| G          | Goal               |
| █ (yellow) | Warehouse Boundary |
| █ (Red)    | Obstacle           |
| .          | Empty Space        |

---

## Algorithms Used

### Breadth-First Search (BFS)

Before the game starts, the simulator checks whether the robot can reach the goal.

If the randomly generated warehouse has no possible route, a new map is generated automatically until a valid path exists.

This guarantees that every game is winnable.

---

## Technologies

* Python
* Random Module
* Terminal ANSI Colors
* Breadth-First Search (BFS)

---

## Project Structure

```
warehouse_robot_simulator.py
README.md
LICENSE
.gitignore
```

## Learning Outcomes

This project strengthened my understanding of:

* Functions
* Lists
* Tuples
* Sets
* Coordinate systems
* Grid-based movement
* Collision detection
* Breadth-First Search (BFS)
* Queue-based algorithms
* Random map generation
* Modular programming

---

## Author

V.Akshaj Ram charan

This repository documents my journey from a manually controlled warehouse simulator to an autonomous warehouse navigation system.







## Screenshots

### Game Start

![Game Start](images/game.start.png)

### Gameplay

![Gameplay](images/middle.game.png)
