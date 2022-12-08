import heapq # used to implement front

#  Dijkstra’s Algorithm on Nodes and Edges
inf = float('inf')

def djikstra(graph, start, end):
    visited = set()
    pathway = {}
    distance = {i: inf for i in range(len(graph))}
    front = []
    heapq.heappush(front, (0, start, None))

    while front:
        # Choose node, n, with lowest cost
        cost, node, predecessor = heapq.heappop(front)
        
        if node in visited:
                continue # Unvisited neighbours

        # Add to visited set
        visited.add((cost, node, predecessor))

        print(f"I'm at node {node}")
        for neighbour, difference in enumerate(graph[node]):
            # Look at all unvisited neighbours
            if neighbour in visited:
                continue

            print(f'DEBUG: neighbour:{neighbour} difference:{difference}')
            adjustedCost = cost + graph[node][neighbour]
            print(f'{node} -> {neighbour}: {adjustedCost}')
            

            # Adjust cost when new cost is lower
            if adjustedCost < distance[neighbour]:
                distance[neighbour] = adjustedCost
                pathway[neighbour] = node
                heapq.heappush(front, (adjustedCost, neighbour, node))

        print(f'Front: {front}')
        print(f'Visited: {visited}')

    print(f'Distance: {distance}')
    
    # Visualise pathway

    steps = [end]
    current = end
    while current != start:
        current = pathway[current]
        steps.append(current)
    steps.reverse()

    print(f'To get from: {start} -> {end}: {steps}')


# Map implementation
# i.e. graph[1][2] gives cost node 1 -> node 2

task1_graph = [
    [0, 1, inf, 1, inf],
    [1, 0, 4, 1, inf],
    [inf, 4, 0, 1, 4],
    [1, 1, 1, 0, 2],
    [inf, inf, 4, 2, 0]
]


djikstra(task1_graph, 0, 4)