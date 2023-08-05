def Kruskal(N, edges):
    num = 0
    min_cost = 0
    A = [i for i in range(N)]
    edges.sort()
    for edge in edges:
        v1 = edge[1] - 1
        v2 = edge[2] - 1
        if A[v1] != A[v2]:
            min_cost += edge[0]
            num += 1
            element = A[v2]
            for r in range(N):
                if A[r] == element:
                    A[r]= A[v1]
            if num == N - 1:
                return min_cost
    return -1

N, C = (int(x) for x in input().split())
nodes = []
edges = []   
for t in range(N):
    a, b = [int(x) for x in input().split()]
    nodes.append((a,b))
for i in range(N):
    for j in  range(N):
        if i < j:
            weight = (nodes[i][0] - nodes[j][0])**2 + (nodes[i][1] - nodes[j][1])**2
            if weight >= C:
                edges.append((weight, i+1, j+1))

print(Kruskal(N, edges))



