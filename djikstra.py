import heapq # Used to implement front
import math # Used to calculate sqrt(2)

#  Dijkstra’s Algorithm on Nodes and Edges
inf = float('inf')
r2 = math.sqrt(2)

def djikstra(graph, start, end):
    visited = set()
    pathway = {}
    distance = {i+1: inf for i in range(len(graph))}
    front = [] # [g, n, predecessor]

    # Initialise frontier
    heapq.heappush(front, (0, start, None))

    while front:
        # Choose node, n, with lowest cost
        cost, node, predecessor = heapq.heappop(front)
        
        if node in visited:
                continue # Unvisited neighbours

        # Add to visited set
        visited.add((cost, node, predecessor))

        # print(f"I'm at node {node}")
        for neighbour in graph[node]:
            # Look at all unvisited neighbours
            if neighbour in visited:
                continue

            # Updated cost = cost + path length
            # f = g
            travel_dist = cost + graph[node][neighbour]
            
            # print(f'{node} -> {neighbour}: {travel_dist}')

            # Adjust cost when new cost is lower
            if travel_dist < distance[neighbour]:
                distance[neighbour] = travel_dist
                pathway[neighbour] = node
                heapq.heappush(front, (travel_dist, neighbour, node))

        # print(f'Front: {front}')
        # print(f'Visited: {visited}')

    print(f'\n\nShortest distances from {start}: {distance}')
    
    # Visualise pathway

    steps = [end]
    current = end
    while current != start:
        current = pathway[current]
        steps.append(current)
    steps.reverse()

    print(f'To get from: {start} -> {end}\nVisit:{steps}')
