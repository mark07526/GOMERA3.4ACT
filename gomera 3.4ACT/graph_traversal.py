# ==================================================
# ASSESSMENT 3.4: Diagram 2 - Graph Traversal
# ==================================================

network_graph = {
    "A": ["B", "C", "E"],
    "B": ["D", "E"],
    "C": ["E", "F"],
    "D": ["G"],
    "E": ["C", "G"],
    "F": ["G"],
    "G": ["D"]
}


def bfs(graph, start_node):
    queue = [start_node]
    visited = {start_node}
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print("BFS Traversal: " + " -> ".join(result))


def dfs_recursive(graph, current, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []

    visited.add(current)
    result.append(current)

    for neighbor in graph.get(current, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)

    return result


if __name__ == "__main__":
    print("--- DIAGRAM 2: Graph Traversal ---")
    bfs(network_graph, "A")  # Expected: A -> B -> E -> C -> F -> G -> D

    dfs_res = dfs_recursive(network_graph, "A")
    print("DFS Traversal: " + " -> ".join(dfs_res))  # Expected: A -> B -> D -> G -> E -> C -> F