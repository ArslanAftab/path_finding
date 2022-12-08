import heapq # Used to implement front
import math # Used to calculate sqrt(2)

#  Dijkstra’s Algorithm on Nodes and Edges
inf = float('inf')
r2 = math.sqrt(2)

def djikstra(graph, start, end):
    visited = set()
    pathway = {}
    distance = {i+1: inf for i in range(len(graph))}
    front = []
    heapq.heappush(front, (0, start, None))
    print(distance)
    while front:
        # Choose node, n, with lowest cost
        cost, node, predecessor = heapq.heappop(front)
        
        if node in visited:
                continue # Unvisited neighbours

        # Add to visited set
        visited.add((cost, node, predecessor))

        print(f"I'm at node {node}")
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

    print(f'\n\nShortest distances from {start}: {distance}')
    
    # Visualise pathway

    steps = [end]
    current = end
    while current != start:
        current = pathway[current]
        steps.append(current)
    steps.reverse()

    print(f'To get from: {start} -> {end}\nVisit:{steps}')


# Map implementation
# i.e. graph[1][2] gives cost node 1 -> node 2

graph_task_1 = {
    1: {1:0, 2:1, 4:1},
    2: {2:0, 1:1, 3:4, 4:1},
    3: {3:0, 2:4, 4:1, 5:4},
    4: {4:0, 1:1, 2:1, 3:1, 5:2},
    5: {5:0, 3:4, 4:2}
}

graph_task_2 = {
    1: {1:0, 2:1, 5:1},
    2: {2:0, 1:1, 5:r2, 7:r2, 3:1},
    3: {3:0, 2:1, 7:1, 8:r2, 4:1},
    4: {4:0, 3:1, 7:r2, 8:1},
    5: {5:0, 9:1, 2:r2, 1:1},
    6: {6:0},
    7: {7:0, 11:1, 8:1, 4:r2, 3:1, 2:r2},
    8: {8:0, 7:1, 11:r2, 4:1, 3:r2},
    9: {9:0, 13:1, 14:r2, 5:1},
    10: {10:0},
    11: {11:0, 14:r2, 15:1, 16:r2, 8:r2, 7:1},
    12: {12:0},
    13: {13:0, 14:1, 9:1},
    14: {14:0, 13:1, 15:1, 11:r2},
    15: {15:0, 14:1, 16:1, 11:1},
    16: {16:0, 15:1, 11:r2},
}

djikstra(graph_task_2, 1, 16)