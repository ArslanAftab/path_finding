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

graph_task_1 = {
    1: {1:0, 2:1, 4:1},
    2: {2:0, 1:1, 3:4, 4:1},
    3: {3:0, 2:4, 4:1, 5:4},
    4: {4:0, 1:1, 2:1, 3:1, 5:2},
    5: {5:0, 3:4, 4:2}
}

# Task 1
# Call using djikstra(graph, start, end)
djikstra(graph_task_1, 1, 5)