from collections import deque 
 
def bfs(graph, start): 
    visited = set() 
    queue = deque([start]) 
 
    while queue: 
        node = queue.popleft() 
        if node not in visited: 
            visited.add(node) 
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited) 
 
    return visited 
 
# Тесты 
graph1 = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]} 
assert bfs(graph1, 0) == {0, 1, 2, 3} 
 
graph2 = {0: [1, 3], 1: [2], 2: [0], 3: []} 
assert bfs(graph2, 0) == {0, 1, 2, 3} 
 
graph3 = {0: [1, 2], 1: [3, 4], 2: [4, 5], 3: [], 4: [], 5: []} 
assert bfs(graph3, 0) == {0, 1, 2, 3, 4, 5} 
 
graph4 = {0: [1], 1: [2], 2: [3], 3: [4], 4: []} 