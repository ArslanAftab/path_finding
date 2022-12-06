import heapq # used to implement front

#  Dijkstra’s Algorithm on Nodes and Edges
inf = float('inf')

def djikstra(graph, start, end):
    visited = set()
    pathway = {}
    distance = {i+1: inf for i in range(len(graph))}
    front = []
    heapq.heappush(front, (0, start, start))

    while front:
        # Choose node, n, with lowest cost
        cost, node, predecessor = heapq.heappop(front)
        
        if node in visited:
                continue # Unvisited neighbours

        # Add to visited set
        visited.add((cost, node, predecessor))

        for neighbour in graph[node]:
            # Look at all unvisited neighbours
            if neighbour in visited:
                continue

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

graph = {
    1: {1:0, 2:1, 4:1},
    2: {2:0, 1:1, 3:4, 4:1},
    3: {3:0, 2:4, 4:1, 5:4},
    4: {4:0, 1:1, 2:1, 3:1, 5:2},
    5: {5:0, 3:4, 4:2}
}

djikstra(graph, 1, 5)