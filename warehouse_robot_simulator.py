import os
import random

GREEN = "\033[92m"
BLUE = "\033[94m"
BROWN = "\033[33m"
RED = "\033[91m"
RESET = "\033[0m"

def display_header(moves, attempts):
    print("==============================")
    print(" Warehouse Robot Simulator v1 ")
    print("==============================")
    print("                              ")
    print("Objective: Move the robot (R) to the goal (G) while avoiding obstacles (█).")
    print("                              ")

    print(f"moves: {moves}")
    print(f"attempts: {attempts}")
    print("")

    print("Controls:")
    print(" W - Up")
    print(" A - Left")
    print(" S - Down")
    print(" D - Right")
    print(" Q - Quit")

display_header(moves=0, attempts=0)

moves = 0

NO_OF_OBSTACLES = 100
width = 35
height = 15

warehouse_boundary = []

for y in range(height):
    for x in range(width):
        if y == 0 or y == height - 1 or x == 0 or x == width - 1:
            warehouse_boundary.append((x, y))
            

goal_x = random.randint(1, width - 2)
goal_y = random.randint(1, height - 2) 
goal_position = (goal_x, goal_y)

robot_position = (1, 1)  

while goal_position == robot_position:
    goal_x = random.randint(1, width - 2)
    goal_y = random.randint(1, height - 2)
    goal_position = (goal_x, goal_y)

robot_x = robot_position[0]
robot_y = robot_position[1]

def generate_obstacles(number_of_obstacles):
    obstacles = []

    while len(obstacles) < number_of_obstacles:

        obstacle_x = random.randint(1, width - 2)
        obstacle_y = random.randint(1, height - 2)

        obstacle_position = (obstacle_x, obstacle_y)    

        if obstacle_position != robot_position and \
        obstacle_position != goal_position and \
        obstacle_position not in obstacles:

                obstacles.append((obstacle_x, obstacle_y))
    
    return obstacles

          
def can_robot_reach_goal(robot_position, goal_position, obstacles):

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
            if neighbor not in warehouse_boundary and \
            neighbor not in obstacles and \
            neighbor not in visited:
                positions_to_check.append(neighbor)
                visited.add(neighbor)

    return False

            
def display_warehouse(obstacles):
    for y in range(height - 1, -1, -1):
        for x in range(width):

            if (x,y) == robot_position and (x,y) == goal_position:
                print("X", end="")

            elif (x, y) == robot_position:
                print(BLUE + "R" + RESET, end="")

            elif (x, y) == goal_position:
                print(GREEN + "G" + RESET, end="") 

            elif (x, y) in warehouse_boundary:
                print(BROWN + "█" + RESET, end="")

            elif (x, y) in obstacles:
                print(RED + "█" + RESET, end="")

            else:
                print(".", end="")

        print()


attempts = 0

while True:
    
    obstacles = generate_obstacles(NO_OF_OBSTACLES)
    attempts += 1

    if can_robot_reach_goal(robot_position, goal_position, obstacles):
        break
print("map generated in", attempts, "attempts")  


display_warehouse(obstacles)     

while robot_position != goal_position:

    command = input("> ").lower()
    new_x = robot_x
    new_y = robot_y

    if command == "w":
        new_y += 1

    elif command == "s":
        new_y -= 1

    elif command == "a":
        new_x -= 1

    elif command == "d":
        new_x += 1

    elif command == "q":
        print("Quitting the game.")
        break    

    else:
        print("Invalid command. Use w, a, s, or d.")
        continue

    new_position = (new_x, new_y)

    moves += 1

    if new_position in warehouse_boundary:
        print("you cannot move there. the robot is at the warehouse boundary. You LOSE.")
        break
    if new_position in obstacles:
        print("you cannot move there. the robot is at an obstacle. You LOSE.")
        break

    robot_x = new_x
    robot_y = new_y
    robot_position = (robot_x, robot_y) 

    os.system("cls" if os.name == "nt" else "clear")

    display_header(moves, attempts)
    display_warehouse(obstacles)

    if robot_position == goal_position:
        print("Robot has reached the goal position! You WIN!")
        break

    


