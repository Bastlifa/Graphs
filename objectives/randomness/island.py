# islands = [
#     [0, 1, 0, 1, 0],
#     [1, 1, 0, 1, 1],
#     [0, 0, 1, 0, 0],
#     [1, 0, 1, 0, 0],
#     [1, 1, 0, 0, 0]
# ]

# class Graph:
#     def __init__(self):
#         self.vertices = {

#         }
#         self.edges = {}
#         for i in range(len(islands)):
#             for j in range(len(islands[i])):
#                 self.vertices[(i,j): islands[i][j]]

#     def add_vertex(self, vertex_id):
#         self.vertices[vertex_id] = set()

#     def add_edge(self, v1, v2):
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)

#     def get_neighbors(self, vertex_id):
#         return self.vertices[vertex_id]

#     def get_edges():
#         global islands
#         def check_north(island_num, index):
#             if island_num == 0:
#                 return False
#             if islands[island_num - 1][index]:
#                 return True
#         def check_east(island_num, index):
#             if index == 4:
#                 return False
#             if islands[island_num][index + 1]:
#                 return True
#         def check_south(island_num, index):
#             if island_num == 4:
#                 return False
#             if islands[island_num + 1][index]:
#                 return True
#         def check_west(island_num, index):
#             if index == 0:
#                 return False
#             if islands[island_num][index -1]:
#                 return True
#         for i in range(len(islands)):
#             for j in range(len(islands[i])):
#                 if check_north(i, j):
#                     add_edge

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
def get_neighbors(x, y, matrix):
    neighbors = []
    if x > 0 and matrix[y][x - 1] == 1:
        neighbors.append((x - 1, y))
    if x < len(matrix[0]) - 1 and matrix[y][x + 1] == 1:
        neighbors.append((x + 1, y))
    if y > 0 and matrix[y - 1][x] == 1:
        neighbors.append((x, y - 1))
    if y < len(matrix) - 1 and matrix[y + 1][x] == 1:
        neighbors.append((x, y + 1))
    return neighbors
def dfs(x, y, matrix, visited):
    s = Stack()
    s.push((x, y))
    while s.size() > 0:
        v = s.pop()
        if not visited[v[1]][v[0]]:
            visited[v[1]][v[0]] = True
            for neighbor in get_neighbors(v[0], v[1], matrix):
                s.push(neighbor)
    return visited
def island_counter(matrix):
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    island_count = 0
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if not visited[y][x]:
                if matrix[y][x] == 1:
                    visited = dfs(x, y, matrix, visited)
                    island_count += 1
                else:
                    visited[y][x] = True
    return island_count
def print_matrix(matrix):
    for row in matrix:
        print("".join([str(i) for i in row]))
matrix = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 1, 0, 1], [0, 0, 1, 0, 0, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1, 0, 1, 1, 0], [0, 1, 0, 1, 1, 1, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 1, 0, 0, 0], [1, 0, 1, 1, 0, 0, 0, 1, 1, 0], [0, 1, 1, 0, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]
print_matrix(matrix)
island_counter(matrix)