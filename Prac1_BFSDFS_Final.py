from collections import deque
class Graph:
    def __init__(self, v):
        self.adj = [[] for _ in range(v)]

    def add_edge(self, v, w):
        self.adj[v].append(w)

    def dfs_recursive(self, vertex, visited=set()):
        visited.add(vertex)
        print(vertex, end=" ")

        for neighbor in self.adj[vertex]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def bfs_recursive(self, queue, visited=set()):
        
        if not queue:
            return

        s = queue.popleft()
        if s not in visited:
            print(s, end=" ")
            visited.add(s)
            queue.extend(self.adj[s])
        self.bfs_recursive(queue, visited)


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
g.dfs_recursive(start)
print("\nBFS of Graph:")
g.bfs_recursive(deque([start]))
