import heapq

# Grid setup
GRID_SIZE = int(input("Enter grid size (e.g., 4 for 4x4 grid): "))
grid = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Place Wumpus
wumpus_count = int(input("Enter number of Wumpus: "))
for _ in range(wumpus_count):
    x, y = map(int, input("Enter Wumpus position (row col, 0-based index): ").split())
    grid[x][y] = 'W'

# Place Pits
pit_count = int(input("Enter number of Pits: "))
for _ in range(pit_count):
    x, y = map(int, input("Enter Pit position (row col, 0-based index): ").split())
    grid[x][y] = 'P'

# Place Gold
gold_x, gold_y = map(int, input("Enter Gold position (row col, 0-based index): ").split())
grid[gold_x][gold_y] = 'G'

# Agent's starting position
agent_pos = tuple(map(int, input("Enter agent's starting position (row col, 0-based index): ").split()))
grid[agent_pos[0]][agent_pos[1]] = 'A'

# Knowledge Base
KB = {agent_pos: {'Safe': True, 'Wumpus?': False, 'Pit?': False, 'Visited': True}}

# Get percepts for a position
def get_percepts(pos):
    x, y = pos
    percepts = []
    if 'G' in grid[x][y]:
        percepts.append('Glitter')
    if 'W' in get_adjacent(x, y):
        percepts.append('Stench')
    if 'P' in get_adjacent(x, y):
        percepts.append('Breeze')
    return percepts

# Get adjacent cells
def get_adjacent(x, y):
    adjacent = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
            adjacent.append(grid[nx][ny])
    return adjacent

# Update KB
def update_kb(pos, percepts):
    if pos not in KB:
        KB[pos] = {'Safe': True, 'Wumpus?': False, 'Pit?': False, 'Visited': False}
    KB[pos]['Visited'] = True

    if 'Breeze' in percepts:
        mark_adjacent(pos, 'Pit?')
    if 'Stench' in percepts:
        mark_adjacent(pos, 'Wumpus?')

# Mark adjacent cells
def mark_adjacent(pos, hazard):
    x, y = pos
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
            if (nx, ny) not in KB:
                KB[(nx, ny)] = {'Safe': True, 'Wumpus?': False, 'Pit?': False, 'Visited': False}
            KB[(nx, ny)][hazard] = True

# Infer safe cells
def infer_safe_cells():
    new_safe = []
    for pos, info in list(KB.items()):
        if info['Visited'] and not info['Pit?'] and not info['Wumpus?']:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = pos[0] + dx, pos[1] + dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                    if (nx, ny) not in KB:
                        new_safe.append((nx, ny))
    for cell in new_safe:
        KB[cell] = {'Safe': True, 'Wumpus?': False, 'Pit?': False, 'Visited': False}

# A* Pathfinding
def a_star(start, goal):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < GRID_SIZE and 0 <= neighbor[1] < GRID_SIZE:
                # Allow exploration if cell is safe or unexplored (not marked as dangerous)
                if KB.get(neighbor, {}).get('Safe', True) and not KB.get(neighbor, {}).get('Pit?', False) and not KB.get(neighbor, {}).get('Wumpus?', False):
                    tentative_g_score = g_score[current] + 1
                    if tentative_g_score < g_score.get(neighbor, float('inf')):
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        heapq.heappush(open_set, (tentative_g_score + heuristic(neighbor, goal), neighbor))
    return None

# Main loop
while True:
    percepts = get_percepts(agent_pos)
    update_kb(agent_pos, percepts)
    infer_safe_cells()

    print(f"Percepts at {agent_pos}: {percepts}")
    print(f"Knowledge Base: {KB}")

    if 'Glitter' in percepts:
        print("Gold Found! Exiting.")
        break

    if 'P' in grid[agent_pos[0]][agent_pos[1]]:
        print("Fell into a pit! Game Over.")
        break
    if 'W' in grid[agent_pos[0]][agent_pos[1]]:
        print("Eaten by Wumpus! Game Over.")
        break

    # Use A* to find a path to gold
    path_to_gold = a_star(agent_pos, (gold_x, gold_y))
    if path_to_gold:
        print("Safe path to gold using A*:", path_to_gold)
        break
    else:
        print("No path to gold found.")
        break