class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state  # State of the node
        self.parent = parent  # Parent node
        self.g = g  # Cost from start to current node
        self.h = h  # Heuristic cost from current node to goal

    def f(self):
        return self.g + self.h  # Total estimated cost

def a_star(start, goal, grid):
    def heuristic(node):
        x, y = node.state
        goal_x, goal_y = goal
        return abs(goal_x - x) + abs(goal_y - y)  # Manhattan distance heuristic

    open_set = []
    closed_set = set()
    start_node = Node(start, None, 0, heuristic(Node(start)))
    open_set.append(start_node)

    while open_set:
        open_set.sort(key=lambda x: x.f())  # Sort by total cost (f() value)
        current = open_set.pop(0)

        if current.state == goal:
            path = []
            while current:
                path.append(current.state)
                current = current.parent
            return path[::-1]

        closed_set.add(current.state)

        for next_state in neighbors(current.state, grid):
            if next_state in closed_set:
                continue

            g = current.g + 1  # Assuming uniform cost for simplicity
            h = heuristic(Node(next_state))
            neighbor = Node(next_state, current, g, h)

            if neighbor not in open_set:
                open_set.append(neighbor)

    return None

def neighbors(state, grid):
    x, y = state
    all_neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    valid_neighbors = []

    for neighbor in all_neighbors:
        if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
            valid_neighbors.append(neighbor)

    return valid_neighbors

# Take input from user
start_x = int(input("Enter the starting X coordinate: "))
start_y = int(input("Enter the starting Y coordinate: "))
goal_x = int(input("Enter the goal X coordinate: "))
goal_y = int(input("Enter the goal Y coordinate: "))
grid_size = int(input("Enter the grid size (square grid): "))
game_grid = []

for row in range(grid_size):
    grid_row = []
    for col in range(grid_size):
        cell_value = int(input(f"Enter cell value (0 for empty, 1 for blocked) at position ({row}, {col}): "))
        grid_row.append(cell_value)
    game_grid.append(grid_row)

start_cell = (start_x, start_y)
goal_cell = (goal_x, goal_y)

path = a_star(start_cell, goal_cell, game_grid)

if path:
    print("Path found:", path)
else:
    print("No path found")

