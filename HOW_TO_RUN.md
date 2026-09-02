# How to Run

## Requirements

* Python 3.10 or newer
* Windows recommended
* No external Python packages are required

## 1. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/Akshaj-echo/warehouse-robot-simulator.git
cd warehouse-robot-simulator
```

## 2. Run the Simulator

### Windows

```bash
py warehouse_robot_simulator.py
```

If Python is configured correctly in your PATH, this also works:

```bash
python warehouse_robot_simulator.py
```

## 3. Controls

| Key       | Action     |
| --------- | ---------- |
| `W` / `↑` | Move up    |
| `A` / `←` | Move left  |
| `S` / `↓` | Move down  |
| `D` / `→` | Move right |
| `Q`       | Quit       |

## 4. Navigation Modes

When the simulator starts, follow the on-screen menu to select the available navigation mode.

The simulator supports:

* Manual robot control
* Autonomous path planning
* BFS
* Dijkstra
* A*
* Weighted terrain navigation

## Troubleshooting

### IF Python command not recognized

On Windows, try:

```bash
py warehouse_robot_simulator.py
```

instead of:

```bash
python warehouse_robot_simulator.py
```

### IF Repository does not clone

Make sure Git is installed and that you have an internet connection.
