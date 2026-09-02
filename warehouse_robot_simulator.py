import heapq
import math
import os
import random
import msvcrt
import time
from collections import deque


GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[33m"
RED = "\033[91m"
PURPLE = "\033[35m"
RESET = "\033[0m"


class Warehouse:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = []
        self.goal_position = None
        self.boundary = []
        self.walkable_cells = []
        self.terrain_costs = {}

class Robot:

    def __init__(self, x, y):
        self.position = (x, y)

    def move_up(self):
        return (self.position[0], self.position[1] + 1)

    def move_down(self):
        return (self.position[0], self.position[1] - 1)

    def move_left(self):
        return (self.position[0] - 1, self.position[1])

    def move_right(self):
        return (self.position[0] + 1, self.position[1])


def display_header(
        moves,
        attempts,
        difficulty,
        warehouse,
        path_length,
        cells_explored,
        algorithm
):

    print("==============================")
    print(" Warehouse Robot Simulator v3 ")
    print("==============================")
    print()

    print(
        "Objective: Move the robot (R) to the goal (G) "
        "while avoiding obstacles (█)."
    )

    print()

    print(f"Moves: {moves}")
    print(f"Map generated in {attempts} attempts")
    print(f"Difficulty: {difficulty}")
    print(f"Warehouse: {warehouse.width} x {warehouse.height}")

    print()

    print("Controls:")
    print(" W / ↑ - Up")
    print(" A / ← - Left")
    print(" S / ↓ - Down")
    print(" D / → - Right")
    print(" Q - Quit")

    print()

    print("Algorithm:", algorithm)
    print(f"Path length: {path_length}")
    print(f"Cells explored: {cells_explored}")


def generate_warehouse_shape(warehouse):

    center_x = warehouse.width / 2
    center_y = warehouse.height / 2

    number_of_points = random.randint(5, 10)

    angles = sorted(
        [
            random.uniform(0, 2 * math.pi)
            for _ in range(number_of_points)
        ]
    )

    points = []

    for angle in angles:

        radius_x = random.uniform(
            warehouse.width * 0.40,
            warehouse.width * 0.49
        )

        radius_y = random.uniform(
            warehouse.height * 0.40,
            warehouse.height * 0.49
        )

        x = center_x + radius_x * math.cos(angle)
        y = center_y + radius_y * math.sin(angle)

        points.append((x, y))

    walkable_cells = set()

    for y in range(1, warehouse.height - 1):

        for x in range(1, warehouse.width - 1):

            inside = False
            j = len(points) - 1

            for i in range(len(points)):

                xi, yi = points[i]
                xj, yj = points[j]

                if (
                    ((yi > y) != (yj > y))
                    and
                    (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
                ):
                    inside = not inside

                j = i

            if inside:
                walkable_cells.add((x, y))

    warehouse.walkable_cells = list(walkable_cells)

    boundary_cells = set()

    for cell in walkable_cells:

        x, y = cell

        neighbors = [
            (x, y + 1),
            (x, y - 1),
            (x - 1, y),
            (x + 1, y)
        ]

        for neighbor in neighbors:

            if neighbor not in walkable_cells:

                boundary_cells.add(cell)
                break

    warehouse.boundary = list(boundary_cells)


def generate_terrain(warehouse, floor_cells):

    terrain_types = {
        "normal": 1,
        "rough": 3,
        "very_rough": 5
    }

    for cell in floor_cells:

        terrain = random.choices(
            list(terrain_types.keys()),
            weights=[0.60, 0.25, 0.15]
        )[0]

        warehouse.terrain_costs[cell] = terrain_types[terrain]














def generate_obstacles(
        warehouse,
        number_of_obstacles,
        floor_cells,
        robot_position
):

    obstacles = set()

    max_possible = len(floor_cells) - 2

    number_of_obstacles = min(
        number_of_obstacles,
        max_possible
    )

    number_of_obstacles = max(
        number_of_obstacles,
        0
    )

    while len(obstacles) < number_of_obstacles:

        obstacle_position = random.choice(floor_cells)

        if (
            obstacle_position != robot_position
            and
            obstacle_position != warehouse.goal_position
        ):

            obstacles.add(obstacle_position)

    return obstacles




# ============================================================
# BFS
# ============================================================

def bfs(
        robot_position,
        goal_position,
        obstacles,
        warehouse
):

    positions_to_check = deque([robot_position])
    visited = {robot_position}

    previous_position = {}

    while positions_to_check:

        current_position = positions_to_check.popleft()

        if current_position == goal_position:

            path = []

            current = goal_position

            while current != robot_position:

                path.append(current)
                current = previous_position[current]

            path.append(robot_position)

            path.reverse()

            return path, len(visited)

        x = current_position[0]
        y = current_position[1]

        neighbor_positions = [
            (x, y + 1),
            (x, y - 1),
            (x - 1, y),
            (x + 1, y)
        ]

        for neighbor in neighbor_positions:

            if (
                neighbor in warehouse.walkable_cells
                and neighbor not in warehouse.boundary
                and neighbor not in obstacles
                and neighbor not in visited
            ):

                positions_to_check.append(neighbor)
                visited.add(neighbor)

                previous_position[neighbor] = current_position

    return None, len(visited)




#============================================================   
# Dijkstra 
#============================================================

def dijkstra(
        robot_position,
        goal_position,
        obstacles,
        warehouse
):

    priority_queue = [(0, robot_position)]

    distances = {robot_position: 0}

    previous_position = {}

    while priority_queue:

        current_cost, current_position = heapq.heappop(priority_queue)

        if current_position in distances and current_cost > distances[current_position]:
            continue

        if current_position == goal_position:

            path = []

            current = goal_position

            while current != robot_position:

                path.append(current)
                current = previous_position[current]

            path.append(robot_position)

            path.reverse()

            return path, len(distances)

        x = current_position[0]
        y = current_position[1]

        neighbor_positions = [
            (x, y + 1),
            (x, y - 1),
            (x - 1, y),
            (x + 1, y)
        ]

        for neighbor in neighbor_positions:

            if (
                neighbor in warehouse.walkable_cells
                and neighbor not in warehouse.boundary
                and neighbor not in obstacles
            ):

                distance = (
                    current_cost
                    + warehouse.terrain_costs[neighbor]
                )

                if (
                    neighbor not in distances
                    or distance < distances[neighbor]
                ):

                    distances[neighbor] = distance
                    previous_position[neighbor] = current_position

                    heapq.heappush(priority_queue, (distance, neighbor))

    return None, len(distances)



#============================================================
# A* 
#============================================================

def a_star(
        robot_position,
        goal_position,
        obstacles,
        warehouse
):

    priority_queue = [(0, robot_position)]

    distances = {robot_position: 0}
    previous_position = {}

    while priority_queue:

        current_cost, current_position = heapq.heappop(priority_queue)

        if current_position == goal_position:

            path = []

            current = goal_position

            while current != robot_position:

                path.append(current)
                current = previous_position[current]

            path.append(robot_position)

            path.reverse()

            return path, len(distances)
        

        x = current_position[0]
        y = current_position[1]

        neighbor_positions = [
            (x, y + 1),
            (x, y - 1),
            (x - 1, y),
            (x + 1, y)
        ]
        for neighbor in neighbor_positions:

            if (
                neighbor in warehouse.walkable_cells
                and neighbor not in warehouse.boundary
                and neighbor not in obstacles
            ):
                g_cost = (
                    distances[current_position]
                    + warehouse.terrain_costs[neighbor]
                )

                h_cost = (
                    abs(neighbor[0] - goal_position[0])
                    +
                    abs(neighbor[1] - goal_position[1])
                )


                f_cost = g_cost + h_cost


                if (
                    neighbor not in distances
                    or g_cost < distances[neighbor]
                ):
                    distances[neighbor] = g_cost
                    previous_position[neighbor] = current_position
                    heapq.heappush(priority_queue, (f_cost, neighbor))

    return None, 0




def find_path(
        algorithm,
        robot_position,
        goal_position,
        obstacles,
        warehouse
):

    if algorithm == "BFS":

        return bfs(
            robot_position,
            goal_position,
            obstacles,
            warehouse
        )

    elif algorithm == "Dijkstra":

        return dijkstra(
            robot_position,
            goal_position,
            obstacles,
            warehouse
        )

    elif algorithm == "A*":

        return a_star(
            robot_position,
            goal_position,
            obstacles,
            warehouse
        )

    else:

        return None, 0




def calculate_path_cost(path, warehouse):

    total_cost = 0

    for position in path[1:]:

        total_cost += warehouse.terrain_costs[position]

    return total_cost


def display_warehouse(
        warehouse,
        obstacles,
        robot,
        bfs_path=None,
        dijkstra_path=None,
        astar_path=None,
        path=None,
        mode=None
):
    bfs_path = set(bfs_path or [])
    dijkstra_path = set(dijkstra_path or [])
    astar_path = set(astar_path or [])
    path = set(path or [])

    for y in range(
            warehouse.height - 1,
            -1,
            -1
    ):

        for x in range(warehouse.width):

            position = (x, y)

            if position not in warehouse.walkable_cells:

                print(" ", end="")

            elif position in warehouse.boundary:

                print(
                    YELLOW + "█" + RESET,
                    end=""
                )

            elif (
                position == robot.position
                and
                position == warehouse.goal_position
            ):

                print(
                    YELLOW + "X" + RESET,
                    end=""
                )

            elif position == robot.position:

                print(
                    BLUE + "R" + RESET,
                    end=""
                )

            elif position == warehouse.goal_position:

                print(
                    GREEN + "G" + RESET,
                    end=""
                )

            elif position in obstacles:

                print(
                    RED + "█" + RESET,
                    end=""
                )

            elif (
                position in bfs_path
                and
                position in dijkstra_path
                and
                position in astar_path
            ):

                print(
                    YELLOW + "*" + RESET,
                    end=""
                )

            elif (
                position in bfs_path
                and
                position in dijkstra_path
            ):

                print(
                    BLUE + "*" + RESET,
                    end=""
                )

            elif (
                position in bfs_path
                and
                position in astar_path
            ):

                print(
                    BLUE + "*" + RESET,
                    end=""
                )

            elif (
                position in dijkstra_path
                and
                position in astar_path
            ):

                print(
                    PURPLE + "*" + RESET,
                    end=""
                )

            elif position in path:

                print(
                    GREEN + "*" + RESET,
                    end=""
                )


            elif position in bfs_path:

                print(
                    BLUE + "*" + RESET,
                    end=""
                )

            elif position in dijkstra_path:

                print(
                    PURPLE + "*" + RESET,
                    end=""
                )

            elif position in astar_path:

                print(
                    GREEN + "*" + RESET,
                    end=""
                )

            else:
                    if mode == "Manual":
                        print(".", end="")
                    else:
                        terrain_cost = warehouse.terrain_costs.get(
                            position,
                            1
                        )

                        if terrain_cost == 1:
                            print(".", end="")
                        elif terrain_cost == 3:
                            print("~", end="")
                        elif terrain_cost == 5:
                            print("^", end="")

        print()


def play_game():

    moves = 0

    # ============================================================
    # Generate warehouse
    # ============================================================

    while True:

        warehouse_width = random.randint(40, 60)
        warehouse_height = random.randint(25, 40)

        warehouse = Warehouse(
            warehouse_width,
            warehouse_height
        )

        generate_warehouse_shape(warehouse)

        floor_cells = [
            cell
            for cell in warehouse.walkable_cells
            if cell not in warehouse.boundary
        ]

        generate_terrain(warehouse, floor_cells)


        if len(floor_cells) >= 20:
            break

    # ============================================================
    # Robot
    # ============================================================

    robot_position = random.choice(floor_cells)

    robot = Robot(
        robot_position[0],
        robot_position[1]
    )

    # ============================================================
    # Goal
    # ============================================================

    goal_position = max(
        floor_cells,
        key=lambda cell:
        abs(cell[0] - robot.position[0])
        +
        abs(cell[1] - robot.position[1])
    )

    warehouse.goal_position = goal_position

    # ============================================================
    # Difficulty
    # ============================================================

    while True:

        print("==============================")
        print(" Warehouse Robot Simulator v3 ")
        print("==============================")
        print()

        print(
            "Objective: Move the robot (R) "
            "to the goal (G) while avoiding obstacles (█)."
        )

        print()

        print("Select difficulty:")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")

        difficulty_choice = input("> ")

        if difficulty_choice == "1":

            difficulty = "Easy"
            obstacle_density = 0.10
            break

        elif difficulty_choice == "2":

            difficulty = "Medium"
            obstacle_density = 0.20
            break

        elif difficulty_choice == "3":

            difficulty = "Hard"
            obstacle_density = 0.30
            break

        else:

            print("Invalid choice. Choose 1, 2, or 3.")

    os.system(
        "cls" if os.name == "nt" else "clear"
    )

    # ============================================================
    # Mode
    # ============================================================

    while True:

        print("Select mode:")
        print("1 - Manual")
        print("2 - Autonomous")
        print("3 - Compare Algorithms")

        mode_choice = input("> ")

        if mode_choice == "1":

            mode = "Manual"
            break

        elif mode_choice == "2":

            mode = "Autonomous"
            break

        elif mode_choice == "3":

            mode = "Comparison"
            break

        elif mode_choice == "q":

            print("Quitting the game.")
            return False

        else:

            print("Invalid choice. Choose 1 or 2.")

    os.system(
        "cls" if os.name == "nt" else "clear"
    )

    # ============================================================
    # Algorithm selection
    # ============================================================

    if mode == "Autonomous":

        while True:

            print("Select algorithm:")
            print("1 - BFS")
            print("2 - Dijkstra")
            print("3 - A*")

            algorithm_choice = input("> ").lower()

            if algorithm_choice == "1":

                algorithm = "BFS"
                break

            elif algorithm_choice == "2":

                algorithm = "Dijkstra"
                break

            elif algorithm_choice == "3":

                algorithm = "A*"
                break
            
            elif algorithm_choice == "q":

                print("Quitting the game.")
                return False   

            else:

                print("Invalid choice. Choose 1, 2, or 3.")

    else:

        algorithm = "None"

    os.system(
        "cls" if os.name == "nt" else "clear"
    )

    # ============================================================
    # Obstacles
    # ============================================================

    number_of_obstacles = int(
        len(floor_cells) * obstacle_density
    )

    # ============================================================
    # Generate valid map + calculate path
    # ============================================================
    attempts = 0

    path = None
    cells_explored = 0

    while True:

        warehouse.obstacles = generate_obstacles(
            warehouse,
            number_of_obstacles,
            floor_cells,
            robot.position
        )

        attempts += 1


        
        if mode != "Comparison":

            if mode == "Manual":

                # Use BFS only to verify that the generated
                # warehouse is actually solvable.
                path, cells_explored = bfs(
                    robot.position,
                    warehouse.goal_position,
                    warehouse.obstacles,
                    warehouse
                )

            else:

                path, cells_explored = find_path(
                    algorithm,
                    robot.position,
                    warehouse.goal_position,
                    warehouse.obstacles,
                    warehouse
                )

        if path is not None:
            break

        # Comparison mode
        else:

            bfs_path, bfs_explored = bfs(
                robot.position,
                warehouse.goal_position,
                warehouse.obstacles,
                warehouse
            )

            if bfs_path is not None:
                break



    # ========================================================
    # Run all three algorithms on the SAME map
    # ========================================================    
        # ========================================================
    # Comparison Mode
    # ========================================================


    if mode == "Comparison":

        original_robot_position = robot.position

        while True:

            # ====================================================
            # Run all three algorithms on the SAME map
            # ====================================================

            bfs_path, bfs_explored = bfs(
                original_robot_position,
                warehouse.goal_position,
                warehouse.obstacles,
                warehouse
            )

            dijkstra_path, dijkstra_explored = dijkstra(
                original_robot_position,
                warehouse.goal_position,
                warehouse.obstacles,
                warehouse
            )

            astar_path, astar_explored = a_star(
                original_robot_position,
                warehouse.goal_position,
                warehouse.obstacles,
                warehouse
            )

            # ====================================================
            # Calculate total costs
            # ====================================================

            bfs_cost = calculate_path_cost(
                bfs_path,
                warehouse
            )

            dijkstra_cost = calculate_path_cost(
                dijkstra_path,
                warehouse
            )

            astar_cost = calculate_path_cost(
                astar_path,
                warehouse
            )

            # ====================================================
            # Display comparison
            # ====================================================

            os.system(
                "cls" if os.name == "nt" else "clear"
            )

            print("==============================")
            print(" ALGORITHM COMPARISON")
            print("==============================")

            print()
            print(
                BLUE + "*" + RESET + " = BFS"
            )

            print(
                PURPLE + "*" + RESET + " = Dijkstra"
            )

            print(
                GREEN + "*" + RESET + " = A*"
            )

            print(
                YELLOW + "*" + RESET + " = Shared path"
            )

            print()

            print("BFS")
            print("Path length:", len(bfs_path) - 1)
            print("Total cost:", bfs_cost)
            print("Cells explored:", bfs_explored)

            print()

            print("Dijkstra")
            print("Path length:", len(dijkstra_path) - 1)
            print("Total cost:", dijkstra_cost)
            print("Cells explored:", dijkstra_explored)

            print()

            print("A*")
            print("Path length:", len(astar_path) - 1)
            print("Total cost:", astar_cost)
            print("Cells explored:", astar_explored)

            print()

            print("==============================")
            print(" WAREHOUSE PATHS")
            print("==============================")

            print()

            display_warehouse(
                warehouse,
                warehouse.obstacles,
                robot,
                bfs_path=bfs_path,
                dijkstra_path=dijkstra_path,
                astar_path=astar_path,
                mode=mode
            )

            # ====================================================
            # Choose algorithm
            # ====================================================

            print()
            print("==============================")
            print(" SELECT ROUTE")
            print("==============================")

            print("1 - BFS")
            print("2 - Dijkstra")
            print("3 - A*")
            print("Q - Quit comparison")

            while True:

                choice = input("> ").lower()

                if choice == "1":

                    selected_algorithm = "BFS"
                    selected_path = bfs_path

                    break

                elif choice == "2":

                    selected_algorithm = "Dijkstra"
                    selected_path = dijkstra_path

                    break

                elif choice == "3":

                    selected_algorithm = "A*"
                    selected_path = astar_path

                    break

                elif choice == "q":

                    return False

                else:

                    print(
                        "Invalid choice. Choose 1, 2, 3, or Q."
                    )

            # ====================================================
            # Robot follows selected path
            # ====================================================

            robot.position = original_robot_position
            moves = 0

            print()
            print(
                "Selected:",
                selected_algorithm
            )

            print(
                "Robot starting navigation..."
            )

            time.sleep(1)

            for position in selected_path[1:]:

                robot.position = position
                moves += 1

                os.system(
                    "cls" if os.name == "nt" else "clear"
                )

                print("==============================")
                print(" SELECTED ROUTE")
                print("==============================")

                print(
                    "Algorithm:",
                    selected_algorithm
                )

                print(
                    "Move:",
                    moves
                )

                print()

                display_warehouse(
                    warehouse,
                    warehouse.obstacles,
                    robot,
                    path=selected_path
                )

                time.sleep(0.1)

            print()
            print(
                selected_algorithm,
                "has reached the goal!"
            )

            # ====================================================
            # Reset robot to original position
            # ====================================================

            robot.position = original_robot_position

            print()
            print(
                "Robot reset to starting position."
            )

            print()
            print("==============================")
            print(" TEST ANOTHER ALGORITHM?")
            print("==============================")

            print("1 - Yes")
            print("2 - No")

            while True:

                again = input("> ").lower()

                if again == "1" or again == "y":

                    break

                elif again == "2" or again == "n":

                    return True

                else:

                    print(
                        "Invalid choice. Enter 1 or 2."
                    )




    # ============================================================
    # Find path
    # ============================================================

    if mode == "Comparison":

        path = bfs_path
        cells_explored = bfs_explored
        algorithm = "Comparison"

    if path:

        path_length = len(path) - 1

    else:

        path_length = 0

    # ============================================================
    # Initial display
    # ============================================================

    display_header(
        moves,
        attempts,
        difficulty,
        warehouse,
        path_length,
        cells_explored,
        algorithm
    )

    print()

    os.system("cls" if os.name == "nt" else "clear")

    if mode == "Manual":

        display_warehouse(
            warehouse,
            warehouse.obstacles,
            robot,
            mode=mode
        )

    else:

        display_warehouse(
            warehouse,
            warehouse.obstacles,
            robot,
            path,
            mode=mode)

# ============================================================
# Autonomous mode
# ============================================================

    if mode == "Autonomous":

        for position in path[1:]:

            robot.position = position
            moves += 1

            os.system(
                "cls" if os.name == "nt" else "clear"
            )

            display_header(
                moves,
                attempts,
                difficulty,
                warehouse,
                path_length,
                cells_explored,
                algorithm
            )

            print()

            display_warehouse(
                warehouse,
                warehouse.obstacles,
                robot,
                path=path,
                mode=mode
            )

            time.sleep(0.1)

        print()
        print("Robot has reached the goal position!")
        print("You WIN!")




        
 
    # ============================================================
    # Manual mode
    # ============================================================

    if mode == "Manual":

        while robot.position != warehouse.goal_position:

            key = msvcrt.getch()

            # WASD
            if key == b'w':

                command = "w"

            elif key == b's':

                command = "s"

            elif key == b'a':

                command = "a"

            elif key == b'd':

                command = "d"

            elif key == b'q':

                command = "q"

            # Arrow keys
            elif key == b'\xe0':

                key = msvcrt.getch()

                if key == b'H':
                    command = "w"

                elif key == b'P':
                    command = "s"

                elif key == b'K':
                    command = "a"

                elif key == b'M':
                    command = "d"

                else:
                    continue

            else:

                continue

            # Quit
            if command == "q":

                print("Quitting the game.")
                break

            # Movement
            elif command == "w":

                new_position = robot.move_up()

            elif command == "s":

                new_position = robot.move_down()

            elif command == "a":

                new_position = robot.move_left()

            elif command == "d":

                new_position = robot.move_right()

            moves += 1

            # Boundary
            if new_position in warehouse.boundary:

                print(
                    "You cannot move there. "
                    "The robot is at the warehouse boundary. "
                    "You LOSE."
                )

                break

            # Obstacle
            if new_position in warehouse.obstacles:

                print(
                    "You cannot move there. "
                    "The robot is at an obstacle. "
                    "You LOSE."
                )

                break

            # Outside warehouse
            if new_position not in warehouse.walkable_cells:

                print(
                    "You cannot move outside "
                    "the warehouse. You LOSE."
                )

                break

            # Move robot
            robot.position = new_position

            os.system(
                "cls" if os.name == "nt" else "clear"
            )

            display_header(
                moves,
                attempts,
                difficulty,
                warehouse,
                path_length,
                cells_explored,
                algorithm
            )

            print()

            display_warehouse(
                warehouse,
                warehouse.obstacles,
                robot,
                mode=mode
                
            )

            # Win
            if robot.position == warehouse.goal_position:

                print()
                print("Robot has reached the goal position!")
                print("You WIN!")

                break




# ============================================================
# Main game loop
# ============================================================

while True:

    result = play_game()

    if result == False:
        break

    play_again = input(
        "\nPlay again? (y/n): "
    ).lower()

    if play_again in ("n", "no"):

        print("Thank you for playing! Goodbye.")
        print("GAME OVER")

        break

    elif play_again in ("y", "yes"):

        os.system(
            "cls" if os.name == "nt" else "clear"
        )

    else:

        print("Invalid input. Game over.")

        break