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

# Task 3
# Call using djikstra(graph, start, end)
print(f'Djikstra algorithm')
djikstra(graph_task_3_1, 5, 32)
print('_'*20)