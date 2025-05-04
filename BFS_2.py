from collections import deque

# Undirected Graph using Adjacency List
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()

def bfs_recursive(queue):
    if not queue:
        return

    current = queue.popleft()
    print(current)
    visited.add(current)

    for neighbor in graph[current]:
        if neighbor not in visited and neighbor not in queue:
            queue.append(neighbor)

    bfs_recursive(queue)

# Initialize queue with starting node
start_node = 'A'
bfs_recursive(deque([start_node]))
