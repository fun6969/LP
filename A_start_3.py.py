# Undirected graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2)],
    'E': [('B', 5), ('F', 1)],
    'F': [('C', 3), ('E', 1)]
}

# Heuristic: estimated cost to goal
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 0  # Goal
}

def a_star(graph, start, goal):
    open_list = [start]
    came_from = {}
    g_score = {start: 0}

    while open_list:
        # Find node in open_list with lowest f = g + h
        current = min(open_list, key=lambda node: g_score.get(node, float('inf')) + heuristic[node])

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        open_list.remove(current)

        for neighbor, cost in graph[current]:
            tentative_g = g_score[current] + cost
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                if neighbor not in open_list:
                    open_list.append(neighbor)

    return None

# Run
path = a_star(graph, 'A', 'F')
if path:
    print("Path found:", path)
else:
    print("No path found.")
