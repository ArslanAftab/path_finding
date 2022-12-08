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

            adjustedCost = cost + graph[node][neighbour]
            
            # print(f'{node} -> {neighbour}: {adjustedCost}')

            # Adjust cost when new cost is lower
            if adjustedCost < distance[neighbour]:
                distance[neighbour] = adjustedCost
                pathway[neighbour] = node
                heapq.heappush(front, (adjustedCost, neighbour, node))

        # print(f'Front: {front}')
        # print(f'Visited: {visited}')

    # print(f'\n\nShortest distances from {start}: {distance}')
    
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

graph_task_3_1 = {
    1: {1:0, 7:1, 8:r2},
    2: {2:0, },
    3: {3:0, 8:r2, 9:1, 4:1},
    4: {4:0, 3:1, 9:r2, 5:1},
    5: {5:0, 4:1, 12:r2, 6:1},
    6: {6:0, 5:1, 12:1},
    7: {7:0, 1:1, 13:1, 14:r2, 8:1},
    8: {8:0, 1:r2, 7:1, 13:r2, 14:1, 15:r2, 9:1, 3:r2},
    9: {9:0, 8:1, 14:r2, 15:1, 16:r2, 4:r2, 3:1},
    10: {10:0, },
    11: {11:0, },
    12: {12:0, 5:r2, 6:1, 17:r2, 18:1},
    13: {13:0, 7:1, 19:1, 14:1, 8:r2},
    14: {14:0, 7:r2, 13:1, 19:r2, 15:1, 9:r2, 8:1},
    15: {15:0, 8:r2, 14:1, 22:r2, 16:1, 9:1},
    16: {16:0, 9:r2, 15:1, 22:1, 23:r2, 17:1, },
    17: {17:0, 16:1, 22:r2, 23:1, 24:r2, 18:1, 12:r2},
    18: {18:0, 17:1, 23:r2, 24:1, 12:1},
    19: {19:0, 25:1, 26:r2, 14:r2, 13:1},
    20: {20:0, },
    21: {21:0, },
    22: {22:0, 15:r2, 28:1, 29:r2, 23:1, 17:r2, 16:1},
    23: {23:0, 16:r2, 22:1, 28:r2, 29:1, 30:r2, 24:1, 18:r2, 17:1},
    24: {24:0, 17:r2, 23:1, 29:r2, 30:1, 18:1},
    25: {25:0, 31:1, 32:r2, 26:1, 19:1},
    26: {26:0, 19:r2, 25:1, 31:r2, 32:1, 33:r2},
    27: {27:0, },
    28: {28:0, 33:r2, 34:1, 35:r2, 29:1, 23:r2, 22:1},
    29: {29:0, 22:r2, 28:1, 34:r2, 35:1, 36:r2, 30:1, 24:r2, 23:1},
    30: {30:0, 23:r2, 29:1, 35:r2, 36:1, 24:1, 23:r2},
    31: {31:0, 32:1, 26:r2, 25:1},
    32: {32:0, 25:r2, 31:1, 33:1, 26:1},
    33: {33:0, 26:r2, 32:1, 34:1, 28:r2},
    34: {34:0, 33:1, 35:1, 29:r2, 28:1},
    35: {35:0, 28:r2, 34:1, 36:1, 30:r2, 29:1},
    36: {36:0, 29:r2, 35:1, 30:1},
}

graph_task_3_2 = {
    1: {1:0, 7:1, 8:r2},
    2: {2:0, },
    3: {3:0, 8:r2, 9:1, 4:1},
    4: {4:0, 3:1, 9:r2, 5:1},
    5: {5:0, 4:1, 12:r2, 6:1},
    6: {6:0, 5:1, 12:1},
    7: {7:0, 1:1, 13:1, 14:r2, 8:1},
    8: {8:0, 1:r2, 7:1, 13:r2, 14:1, 15:r2, 9:1, 3:r2},
    9: {9:0, 8:1, 14:r2, 15:1, 16:r2, 4:r2, 3:1},
    10: {10:0, },
    11: {11:0, },
    12: {12:0, 5:r2, 6:1, 17:r2, 18:1},
    13: {13:0, 7:1, 19:1, 14:1, 8:r2},
    14: {14:0, 7:r2, 13:1, 19:r2, 15:1, 9:r2, 8:1},
    15: {15:0, 8:r2, 14:1, 22:r2, 16:1, 9:1},
    16: {16:0, 9:r2, 15:1, 22:1, 23:r2, 17:1, },
    17: {17:0, 16:1, 22:r2, 23:1, 24:r2, 18:1, 12:r2},
    18: {18:0, 17:1, 23:r2, 24:1, 12:1},
    19: {19:0, 25:1, 26:r2, 14:r2, 13:1},
    20: {20:0, },
    21: {21:0, },
    22: {22:0, 15:r2, 28:1, 29:r2, 23:1, 17:r2, 16:1},
    23: {23:0, 16:r2, 22:1, 28:r2, 29:1, 30:r2, 24:1, 18:r2, 17:1},
    24: {24:0, 17:r2, 23:1, 29:r2, 30:1, 18:1},
    25: {25:0, 31:1, 32:r2, 26:1, 19:1},
    26: {26:0, 19:r2, 25:1, 31:r2, 32:1},
    27: {27:0, },
    28: {28:0, 34:1, 35:r2, 29:1, 23:r2, 22:1},
    29: {29:0, 22:r2, 28:1, 34:r2, 35:1, 36:r2, 30:1, 24:r2, 23:1},
    30: {30:0, 23:r2, 29:1, 35:r2, 36:1, 24:1, 23:r2},
    31: {31:0, 32:1, 26:r2, 25:1},
    32: {32:0, 25:r2, 31:1, 26:1},
    33: {33:0, },
    34: {34:0, 35:1, 29:r2, 28:1},
    35: {35:0, 28:r2, 34:1, 36:1, 30:r2, 29:1},
    36: {36:0, 29:r2, 35:1, 30:1},
}

# Task 1
djikstra(graph_task_1, 1, 5)

# Task 2
djikstra(graph_task_2, 1, 16)

# Task 3.1
djikstra(graph_task_3_1, 5, 32)

# Task 3.2
djikstra(graph_task_3_2, 5, 32)
