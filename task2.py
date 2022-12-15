import heapq # Used to implement front
import math # Used to calculate sqrt(2)

# THIS IS OUR IMPLEMENTATION!!!
from djikstra import djikstra 
# NOT A LIBRARY!!!

#  Dijkstra’s Algorithm on Nodes and Edges
inf = float('inf')
r2 = math.sqrt(2)

# Map implementation
# i.e. graph[1][2] gives cost node 1 -> node 2

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

# Task 2
# Call using djikstra(graph, start, end)
print(f'Djikstra algorithm')
djikstra(graph_task_2, 1, 16)
print('_'*20)
