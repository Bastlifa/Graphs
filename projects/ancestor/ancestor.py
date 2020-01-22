import os
import sys
sys.path.append('../graph')
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for i in range(1, 12):
        g.add_vertex(i)

    for a in ancestors:
        g.add_edge(a[0], a[1])
    paths = []
    for a in g.vertices:
        if g.dfs_recursive(a, starting_node) is not None and\
            len(g.dfs_recursive(a, starting_node)) > 0:
            paths.append(g.dfs_recursive(a, starting_node))
    
    if len(paths) == 1: return -1

    ret_path = paths[0]
    for p in paths:
        if len(p) > len(ret_path) or\
        (len(p) == len(ret_path) and p[0] < ret_path[0]):
            ret_path = p
    
    return ret_path[0]

# def testing_thing():
#     g = Graph()
#     for i in range(1, 12):
#         g.add_vertex(i)

#     test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
#     for a in test_ancestors:
#         g.add_edge(a[0], a[1])
#     paths = []
#     for a in g.vertices:
#         if g.dfs(a, 6) is not None:
#             paths.append(g.dfs(a, 6))
    
#     ret_path = paths[0]
#     for p in paths:
#         if len(p) > len(ret_path) or\
#         (len(p) == len(ret_path) and p[0] < ret_path[0]):
#             ret_path = p

#     return p

# print(testing_thing())