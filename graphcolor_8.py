def is_safe(node , chosen_color , assignment , graph):
    for neighbour in graph[node]:
        if neighbour in assignment and assignment[neighbour]==chosen_color:
            return False
        return True

def graph_color(graph , option_color , assignment={} , node=0 ):
    if node==len(graph):
        return assignment
    
    for chosen_color in option_color:
        if is_safe(node, chosen_color , assignment , graph ):
            assignment[node]=chosen_color
            result= graph_color(graph , option_color , assignment , node+1)
            if result:
                return result
            del assignment[node]
    
    return node

graph={
    0:[1,2],
    1:[0,2,3],
    2:[0,1,3],
    3:[1,2]
}

option_colors=["red","green","blue"]

solution=graph_color(graph,option_colors)
if solution:
    for node,assigned_color in solution.items():
        print(f"node {node} : {assigned_color}")
