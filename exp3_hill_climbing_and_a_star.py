"""
EXPERIMENT 3 — HILL CLIMBING & A* ALGORITHM
Source: 22IT702 LAB MANUAL (Pages 5–7)
Combined 3A and 3B without 'def'
"""

import heapq

# ============================================================
# EXPERIMENT 3A — HILL CLIMBING
# ============================================================
print("--- EXPERIMENT 3A: Hill Climbing ---")
current = 0

while current < 10:
    print("Current State:", current)
    current += 1

print("Goal State Reached:", current)


# ============================================================
# EXPERIMENT 3B — A* ALGORITHM
# ============================================================
print("\n--- EXPERIMENT 3B: A* Algorithm ---")

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 5},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

start = 'A'
goal = 'F'

open_list = []
heapq.heappush(open_list, (0, start))

g_cost = {start: 0}
parent = {start: None}
path = None

while open_list:
    _, current_node = heapq.heappop(open_list)

    if current_node == goal:
        path = []
        curr = current_node
        while curr is not None:
            path.append(curr)
            curr = parent[curr]
        path = path[::-1]
        break

    for neighbor, cost in graph[current_node].items():
        new_cost = g_cost[current_node] + cost

        if neighbor not in g_cost or new_cost < g_cost[neighbor]:
            g_cost[neighbor] = new_cost
            f_cost = new_cost + heuristic[neighbor]
            heapq.heappush(open_list, (f_cost, neighbor))
            parent[neighbor] = current_node

print("Path:", path)
