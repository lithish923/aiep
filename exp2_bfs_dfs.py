"""
EXPERIMENT 2 — BREADTH FIRST SEARCH (BFS) AND DEPTH FIRST SEARCH (DFS)
Source: 22IT702 LAB MANUAL (Pages 3–4)
Note: Implemented procedurally without 'def'
"""

from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# ----------------- BFS TRAVERSAL -----------------
print("BFS Traversal:")
visited_bfs = set()
queue = deque(['A'])

while queue:
    node = queue.popleft()
    if node not in visited_bfs:
        print(node, end=" ")
        visited_bfs.add(node)
        queue.extend(graph[node])

# ----------------- DFS TRAVERSAL -----------------
print("\nDFS Traversal:")
visited_dfs = set()
stack = ['A']

while stack:
    node = stack.pop()
    if node not in visited_dfs:
        print(node, end=" ")
        visited_dfs.add(node)
        # Add neighbors in reverse order to explore left-to-right
        for neighbor in reversed(graph[node]):
            if neighbor not in visited_dfs:
                stack.append(neighbor)

print()
