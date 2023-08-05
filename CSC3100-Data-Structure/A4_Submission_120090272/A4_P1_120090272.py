class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
cnt = 0
n = int(input())
ans = input().split(' ')
nodes = []
for i in ans:
    nodes.append(Node(int(i)))

for n in nodes:
    idx_c = input().split(' ')
    if idx_c[0] == '-1':
        n.left = None
    else:
        n.left = (nodes[int(idx_c[0])-1])
    if idx_c[1] == '-1':
        n.right = None
    else:
        n.right = (nodes[int(idx_c[1])-1])

def is_symmetric(idx_l, idx_r):
    global cnt
    if idx_l == None and idx_r != None:
        return False
    elif idx_l != None and idx_r == None:
        return False
    else:
        if idx_l == idx_r:
            return True
        elif idx_l.key == idx_r.key:
            cnt += 1
            return is_symmetric(idx_l.left, idx_r.right) == True and is_symmetric(idx_l.right, idx_r.left) == True 
        else: 
            return False

ans = 0
for i in nodes:
    cnt = 1
    is_symmetric(i.left, i.right)
    if is_symmetric(i.left, i.right) == False:
        cnt = 0
    ans = max(ans, cnt)
print(ans)