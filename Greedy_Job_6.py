def dfs(graph,start,visited=None):
    if visited is None:
        visited=set()

    visited.add(start)
    print(start,end=" ")


    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)

graph={
    1:[3,4,2],
    2:[5,6],
    3:[4],
    4:[5],
    5:[6],
    6:[]
}

dfs(graph,1)
