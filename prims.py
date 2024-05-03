INF = 9999999
N = 5
G = [
    [0, 4, 0, 10, 0],
    [4, 0, 1, 2, 0],
    [0, 1, 0, 6, 0],
    [10, 2, 6, 0, 3],
    [0, 0, 0, 3, 0]
]

selected_node = [False] * N
selected_node[0] = True
no_edge = 0
min_weight = 0

print("Edge : Weight\n")
while no_edge < N - 1:
    minimum = INF
    a, b = 0, 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if not selected_node[n] and G[m][n] and G[m][n] < minimum:
                    minimum = G[m][n]
                    a, b = m, n
    print(f"{a}-{b} : {G[a][b]}")
    min_weight += minimum
    selected_node[b] = True
    no_edge += 1

print("Minimum Weight Of the Given Graph is:", min_weight)
print("No of the Edges :", no_edge)
