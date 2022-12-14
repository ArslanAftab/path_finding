import heapq # Used to implement front
import math # Used to calculate sqrt(2)

#  Dijkstra’s Algorithm on Nodes and Edges
inf = float('inf')
r2 = math.sqrt(2)

def astar(graph, start, end, grid_dim):
    visited = set()
    pathway = {}
    distance = {i+1: inf for i in range(len(graph))}
    front = [] # [f, g, n, predecessor]

    # Initialise frontier
    dist = get_distance(start, end, grid_dim)
    heapq.heappush(front, (dist, 0, start, None))

    while front:
        # Choose node, n, with lowest cost
        cost, travel, node, predecessor = heapq.heappop(front)
        
        if node in visited:
                continue # Unvisited neighbours

        # Add to visited set
        visited.add((cost, node, predecessor))

        # print(f"I'm at node {node}")
        for neighbour in graph[node]:
            # Look at all unvisited neighbours
            if neighbour in visited:
                continue

            # Updated cost = cost + path length + euclidian dist 
            # g 
            travel_dist = cost + graph[node][neighbour]
            
            # f = g+h
            adjustedCost = travel_dist + get_distance(neighbour, end, grid_dim)

            # print(f'{node} -> {neighbour}: {travel_dist}')

            # Adjust cost when new cost is lower
            if adjustedCost < distance[neighbour]:
                distance[neighbour] = adjustedCost
                pathway[neighbour] = node
                heapq.heappush(front, (adjustedCost, travel_dist, neighbour, node))

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

def get_coordinate(node_number, dim):
    # Given the node number, and the grid dimensions
    # Return the coordinates of given node
    grid_height, grid_width = dim
    x = node_number // grid_height
    y = node_number % grid_width -1
    return (x,y)

def get_distance(node1,node2, dim):
    # Get node 1 coordinates
    a = get_coordinate(node1, dim)

    # Get node 2 coordinates
    b = get_coordinate(node2, dim)

    # Return euclidian distance
    return math.sqrt( (b[0] - a[0])**2 + (b[1] - a[1])**2 )

# print(get_distance(1,8, (6,6)))
