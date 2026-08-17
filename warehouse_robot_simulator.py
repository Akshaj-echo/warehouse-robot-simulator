import os
import random
import msvcrt

GREEN = "\033[92m"
BLUE = "\033[94m"
BROWN = "\033[33m"
RED = "\033[91m"
RESET = "\033[0m"

def play_game():

    def display_header(moves, attempts, difficulty, warehouse):
        print("==============================")
        print(" Warehouse Robot Simulator v2 ")
        print("==============================")
        print("                              ")
        print("Objective: Move the robot (R) to the goal (G) while avoiding obstacles (█).")
        print("                              ")

        print(f"moves: {moves}")
        print(f"Map generated in {attempts} attempts")
        print(f"Difficulty: {difficulty}")
        print(f"Warehouse: {warehouse.width} x {warehouse.height}")
        print("")

        print("Controls:")  
        print(" W / ↑ - Up")
        print(" A / ← - Left")
        print(" S / ↓ - Down")
        print(" D / → - Right")

        print(" Q - Quit")



    moves = 0

    class Warehouse:

        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.obstacles = []
            self.goal_position = None
            self.boundary = []

            for y in range(self.height):
                for x in range(self.width):
                    if (
                        y == 0
                        or y == self.height - 1
                        or x == 0
                        or x == self.width - 1):

                        self.boundary.append((x, y))


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

    warehouse_width = random.randint(20, 40)
    warehouse_height = random.randint(10, 20)

    warehouse = Warehouse(warehouse_width, warehouse_height)


    robot_x = random.randint(1, warehouse.width - 2)
    robot_y = random.randint(1, warehouse.height - 2)

    robot = Robot(robot_x, robot_y)


    goal_x = random.randint(1, warehouse.width - 2)
    goal_y = random.randint(1, warehouse.height - 2) 
    warehouse.goal_position = (goal_x, goal_y)

    while warehouse.goal_position == robot.position:
        goal_x = random.randint(1, warehouse.width - 2)
        goal_y = random.randint(1, warehouse.height - 2)
        warehouse.goal_position = (goal_x, goal_y)

    while True:
        print("==============================")
        print(" Warehouse Robot Simulator v2 ")
        print("==============================")
        print("                              ")
        print("Objective: Move the robot (R) to the goal (G) while avoiding obstacles (█).")
        print("                              ")
        

        print("Select difficulty:")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")

        difficulty_choice = input("> ")
        os.system("cls" if os.name == "nt" else "clear")
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
            print("Invalid difficulty. choose 1, 2, or 3.")

    interior_area = (warehouse.width - 2) * (warehouse.height - 2)

    number_of_obstacles = int(interior_area * obstacle_density)


    def generate_obstacles(number_of_obstacles):
        obstacles = []

        while len(obstacles) < number_of_obstacles:

            obstacle_x = random.randint(1, warehouse.width - 2)
            obstacle_y = random.randint(1, warehouse.height - 2)

            obstacle_position = (obstacle_x, obstacle_y)    

            if obstacle_position != robot.position and \
            obstacle_position != warehouse.goal_position and \
            obstacle_position not in obstacles:

                    obstacles.append((obstacle_x, obstacle_y))
        
        return obstacles

            
    def can_robot_reach_goal(robot_position, goal_position, obstacles, boundary):

        positions_to_check = [robot_position]
        visited = {robot_position}
        while positions_to_check:

            current_position = positions_to_check.pop(0)

            if current_position == goal_position:
                return True
        

            x = current_position[0]
            y = current_position[1]     

            neighbor_positions = [
                (x, y + 1),  
                (x, y - 1),  
                (x - 1, y),  
                (x + 1, y)   
            ]

            for neighbor in neighbor_positions:
                if neighbor not in boundary and \
                neighbor not in obstacles and \
                neighbor not in visited:
                    positions_to_check.append(neighbor)
                    visited.add(neighbor)

        return False


    def display_warehouse(obstacles):
        for y in range(warehouse.height - 1, -1, -1):
            for x in range(warehouse.width):

                if (x,y) == robot.position and (x,y) == warehouse.goal_position:
                    print("X", end="")

                elif (x, y) == robot.position:
                    print(BLUE + "R" + RESET, end="")

                elif (x, y) == warehouse.goal_position:
                    print(GREEN + "G" + RESET, end="") 

                elif (x, y) in warehouse.boundary:
                    print(BROWN + "█" + RESET, end="")

                elif (x, y) in obstacles:
                    print(RED + "█" + RESET, end="")

                else:
                    print(".", end="")

            print()



    attempts = 0

    while True:
        
        warehouse.obstacles = generate_obstacles(number_of_obstacles)
        attempts += 1

        if can_robot_reach_goal(robot.position, warehouse.goal_position, warehouse.obstacles, warehouse.boundary):
            break


    display_header(moves, attempts, difficulty, warehouse)
    display_warehouse(warehouse.obstacles)     




    while robot.position != warehouse.goal_position:

        key = msvcrt.getch()

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

        if command == "q":
            print("Quitting the game.")
            break

        elif command == "w":
            new_position = robot.move_up()

        elif command == "s":
            new_position = robot.move_down()

        elif command == "a":
            new_position = robot.move_left()

        elif command == "d":
            new_position = robot.move_right()

        moves += 1

        if new_position in warehouse.boundary:
            print("You cannot move there. The robot is at the warehouse boundary. You LOSE.")
            break

        if new_position in warehouse.obstacles:
            print("You cannot move there. The robot is at an obstacle. You LOSE.")
            break

        robot.position = new_position

        os.system("cls" if os.name == "nt" else "clear")

        display_header(moves, attempts, difficulty, warehouse)
        display_warehouse(warehouse.obstacles)

        if robot.position == warehouse.goal_position:
            print("Robot has reached the goal position! You WIN!")
            break

while True:

    play_game()

    play_again = input("Play again? (y/n): ").lower()

    if play_again in ("n", "no"):
        print("Thank you for playing! Goodbye.")
        print(" GAME OVER ")
        break

    elif play_again in ("y", "yes"):
        os.system("cls" if os.name == "nt" else "clear")
        continue        