import heapq # used to implement front

#  Dijkstra’s Algorithm on Nodes and Edges

# Represent map as 2d array, i.e. 
# [ Node 1 costs,
#   Node 2 costs, 
#   Node 3 costs,
#  ...] 

inf = float('inf')

map = [
    [0, 1, inf, 1, inf],
    [1, 0, 4, 1, inf],
    [inf, 4, 0, 1, 4],
    [1, 1, 1, 0, 2],
    [inf, inf, 4, 2, 0]
]

def djikstra(map, start, end):
    visited = set()
    front = []
    
    heapq.heappush(front, (0, start, start))

    while front:
        # Consider node, n, in front with lowest cost
        _, node, predecessor = heapq.heappop(front)
        
        # Move n to visited
        visited.add(node)
        
        for neighbourNode, cost in enumerate(map[node]):
            if neighbourNode in visited:
                continue # Unvisited neighbours

            print(f'{node}|{neighbourNode} at: {cost}')

            
            heapq.heappush(front, (cost, neighbourNode, node))

        print(f'Visited: {visited}')
        print(f'Front: {front}')
djikstra(map, 0, 5)