# ==================================================
# ASSESSMENT 3.4: Diagram 1 - Tree Traversal
# ==================================================

tree_graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
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


def dfs_iterative(graph, start_node):
    stack = [start_node]
    visited = set()
    result = []

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.add(current)
            result.append(current)

            neighbors = list(reversed(graph.get(current, [])))
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)

    print("DFS Traversal: " + " -> ".join(result))


if __name__ == "__main__":
    print("--- DIAGRAM 1: Tree Traversal ---")
    bfs(tree_graph, "A")  # Expected: A -> B -> C -> D -> E -> F -> G
    dfs_iterative(tree_graph, "A")  # Expected: A -> B -> D -> E -> C -> F -> G