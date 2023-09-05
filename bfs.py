from collections import deque

def bfs(w):
    global count
    count += 1
    visited[w] = count
    queue.append(w)  # Add w to the queue
    while queue:
        front = queue.popleft()  # Remove front vertex from the queue
        print(f"{front}({visited[front]})", end="\t")
        for j in range(1, v + 1):
            if visited[j] == 0 and mat[front][j] == 1:  # Add all adjacent vertices of 'front' to the queue
                count += 1
                visited[j] = count
                queue.append(j)

def BFS():
    for i in range(1, v + 1):  # Ensures all vertices are visited
        if visited[i] == 0:
            bfs(i)

count = 0
v, e = 0, 0
visited = [0] * 20
mat = [[0] * 20 for _ in range(20)]
queue = deque()

print("Select the type of Graph:")
print("1. Directed Graph")
print("2. Undirected Graph")
ch = int(input())
if ch != 1 and ch != 2:
    print("Invalid option !!")
else:
    v = int(input("Enter the number of vertices: "))
    e = int(input("Enter the number of edges: "))
    print(f"Enter {e} edges one by one:")
    for i in range(e):
        v1, v2 = map(int, input(f"Edge-{i + 1}: ").split())
        if ch == 1:
            mat[v1][v2] = 1  # Directed graph
        else:
            mat[v1][v2] = mat[v2][v1] = 1  # Undirected graph

    print("\nOrder of vertices processed:")
    BFS()
