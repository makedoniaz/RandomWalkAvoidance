import random
import networkx as nx

def random_walk(graph: int, start: int, target = 1, forbidden = 2, num_walks = 100000) -> float:
    # If the start is the target, return 1 (successful)
    if start == target:
        return 1.0
    
    # If the start is the forbidden vertex, return 0 (unsuccessful)
    if start == forbidden:
        return 0.0

    successful_walks = 0

    for _ in range(num_walks):
        current = start
        
        while True:
            neighbors = list(graph.neighbors(current))

            # Check if we hit the forbidden vertex
            if current == forbidden:
                break

            # Check if we reached the target
            if current == target:
                successful_walks += 1
                break

            # Choose the next vertex randomly
            current = random.choice(neighbors)

    return successful_walks / num_walks

# Example usage
graph = nx.Graph()
graph.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 4), (5, 4), (5, 3)])

for k in graph.nodes:
    probability = random_walk(graph, k)
    print(f"For vertex {k}: {probability:.4f}")

