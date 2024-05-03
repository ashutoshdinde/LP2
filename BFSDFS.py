from collections import deque

class Graph:
    def __init__(self, v):
        self.adj = [[] for _ in range(v)]

    def add_edge(self, v, w):
        self.adj[v].append(w)

    def dfs(self, vertex):
        visited = set()
        stack = [vertex]

        while stack:
            v = stack.pop()
            if v not in visited:
                print(v, end=" ")
                visited.add(v)
                stack.extend(reversed(self.adj[v]))

    def bfs(self, s):
        visited = set()
        queue = deque([s])

        while queue:
            s = queue.popleft()
            if s not in visited:
                print(s, end=" ")
                visited.add(s)
                queue.extend(self.adj[s])

n = int(input("Enter the size of the graph: "))
g = Graph(n)

size = int(input("Enter the size of input (edges): "))
for _ in range(size):
    j, k = map(int, input(f"Enter edges {_ + 1} of graph: ").split())

    if j < n and k < n:
        g.add_edge(j, k)
    else:
        print("Invalid Input")

start = int(input("Enter the starting vertex: "))
print("DFS of Graph:")
g.dfs(start)
print("\nBFS of Graph:")
g.bfs(start)
