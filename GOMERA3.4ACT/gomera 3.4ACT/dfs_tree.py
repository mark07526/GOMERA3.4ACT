
tree_graph = {
    "G": ["O", "M"],
    "O": ["E", "R"],
    "M": ["A"],
    "E": [],
    "R": [],
    "A": []
}


# --- DFS Method 1: Preorder (Root -> Left -> Right) ---
def dfs_preorder(graph, node, result=None):
    if result is None:
        result = []
    result.append(node)                      # visit root first
    for child in graph.get(node, []):
        dfs_preorder(graph, child, result)
    return result


# --- DFS Method 2: Inorder (Left -> Root -> Right) ---
def dfs_inorder(graph, node, result=None):
    if result is None:
        result = []
    children = graph.get(node, [])
    left = children[0] if len(children) > 0 else None
    right = children[1] if len(children) > 1 else None

    if left:
        dfs_inorder(graph, left, result)
    result.append(node)                      # visit root between children
    if right:
        dfs_inorder(graph, right, result)
    return result


# --- DFS Method 3: Postorder (Left -> Right -> Root) ---
def dfs_postorder(graph, node, result=None):
    if result is None:
        result = []
    for child in graph.get(node, []):
        dfs_postorder(graph, child, result)
    result.append(node)                      # visit root last
    return result


# --- DFS Method 4: Iterative using a stack ---
def dfs_iterative(graph, start_node):
    stack = [start_node]
    result = []
    while stack:
        current = stack.pop()
        result.append(current)
        for child in reversed(graph.get(current, [])):
            stack.append(child)
    return result


if __name__ == "__main__":
    print("--- ASSESSMENT 3.6: DFS Methods in Tree ---")
    print("Preorder   : " + " -> ".join(dfs_preorder(tree_graph, "G")))    # G O E R M A
    print("Inorder    : " + " -> ".join(dfs_inorder(tree_graph, "G")))     # E O R G A M
    print("Postorder  : " + " -> ".join(dfs_postorder(tree_graph, "G")))   # E R O A M G
    print("Iterative  : " + " -> ".join(dfs_iterative(tree_graph, "G")))   # G O E R M A