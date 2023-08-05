max_n = int(1e6)
inf = 0x3f3f3f3f
edge_num = 0
edge = [Edge() for _ in range(max_n) ]
dir = [0] * max_n
first_p = [inf] * max_n
second_p = [inf] * max_n
col = [False] * max_n

class Edge:
    def __init__(self):
        self.next = 0
        self.point = 0
        self.weight = 0

def append(x, y, z):
    global edge_num
    edge_num += 1
    edge[edge_num].next = dir[x]
    edge[edge_num].point = y
    edge[edge_num].weight = z
    dir[x] = edge_num

def main(edges):
    global edge, first_p, second_p, dir
    for e in edges:
        x, y, z = e
        append(x, y, z)
        append(y, x, z)

    Q = [1] # the Queue to impelemt the 
    col[1] = True
    first_p[1] = 0

    while len(Q) != 0:
        u = Q[0]
        del Q[0]
        col[u] = False
        i = dir[u]
        while i != 0:
            flag = False
            v = edge[i].point
            weight = edge[i].weight
            if first_p[v] > first_p[u] + weight:
                second_p[v] = first_p[v]
                first_p[v] = first_p[u] + weight
                flag = True
            if first_p[v] == first_p[u] + weight and second_p[v] > second_p[u] + weight:
                second_p[v] = second_p[u] + weight
                flag = True
            if first_p[v] < first_p[u] + weight < second_p[v]:
                second_p[v] = first_p[u] + weight
                flag = True
            if flag and not col[v]:
                col[v] = True
                Q.append(v)
            i = edge[i].next
    return second_p[N]

t = [int(i) for i in input().split()]
N, R = t[0], t[1]
edges = []
for r in range(R):
    edges.append(int(i) for i in input().split())
print(main(edges))
