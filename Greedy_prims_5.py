import heapq

def prim_mst(graph, start):
    visited = set()
    min_heap = [(0, start)]  # (weight, vertex)
    total_cost = 0
    mst_edges = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)

        if u in visited:
            continue

        visited.add(u)
        total_cost += weight

        if weight != 0:
            mst_edges.append((u, weight))

        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (w, v))

    return total_cost, mst_edges

# Example graph represented as an adjacency list
# Format: node: [(neighbor, weight), ...]
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4), ('E', 5)],
    'D': [('B', 1), ('C', 4), ('E', 1)],
    'E': [('C', 5), ('D', 1)]
}

# Run Prim's algorithm
cost, mst = prim_mst(graph, 'A')

# Output the results
print("Minimum Spanning Tree edges:")
for node, weight in mst:
    print(f"Node: {node}, Edge Weight: {weight}")
print("Total Cost of MST:", cost)
