"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else: raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
        # pass  # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        """
        create an empty queue, and enqueue the starting vertex ID
        create an empty set to store visited vertices
        while the queue is not empty,
            dequeue the first vertex
            if that vertex has not been visited:
                mark it as visited
                then add all of its neighbors to the back of the queue
        """
        print("BFT print:")
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while len(q.queue) > 0:
            v = q.dequeue()
            if v not in visited:
                visited.add(v)
                print(v)
                for n in self.vertices[v]:
                    q.enqueue(n)
        print("=========================================")
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        """
        create an empty stack, and push the starting vertex ID
        create an empty set to store visited vertices
        while the stack is not empty,
            pop the first vertex
            if that vertex has not been visited:
                mark it as visited
                then add all of its neighbors to the top of the stack
        """
        print("DFT print:")
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print(v)
                for n in self.vertices[v]:
                    s.push(n)
        print("=========================================")

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print("DFT Recursive print:")
        visited = set()
        def dft_rec_inner(sv):
            if sv in visited:
                return
            visited.add(sv)
            print(sv)
            for n in self.vertices[sv]:
                dft_rec_inner(n)
        dft_rec_inner(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        """
        create an empty stack and push a path to the starting vertex ID
        create a set to store visited vertices
        while the stack is not empty:
            pop the first path
            grab the last vertex from the path
            if that vertex has not been visited:
                check if it's the target
                if so:
                    return path
                mark is as visited
                add a path to its neighbors to the back of the stack
                copy the path
                append the neighbor to tha back
        """
        print("BFS Print: ")
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()
        while q.size() > 0:
            last_path = q.dequeue()
            last_v = last_path[-1]
            if last_v not in visited:
                if last_v == destination_vertex:
                    return last_path
                visited.add(last_v)
                for n in self.vertices[last_v]:
                    new_path = [*last_path]
                    new_path.append(n)
                    q.enqueue(new_path)

        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        """
        create an empty queue and enqueue a path to the starting vertex ID
            create a set to store visited vertices
            while the queue is not empty:
                dequeue the first path
                grab the last vertex from the path
                if that vertex has not been visited:
                    check if it's the target
                    if so:
                        return path
                    mark is as visited
                    add a path to its neighbors to the back of the queue
                    copy the path
                    append the neighbor to tha back
        """
        # print("DFS Print: ")
        s = Stack()
        s.push([starting_vertex])
        visited = set()
        while s.size() > 0:
            last_path = s.pop()
            last_v = last_path[-1]
            if last_v not in visited:
                if last_v == destination_vertex:
                    return last_path
                visited.add(last_v)
                for n in self.vertices[last_v]:
                    new_path = [*last_path]
                    new_path.append(n)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # print("DFS Recursive print:")
        visited = set()
        path = []
        def dfs_rec_inner(sv, dv, path):
            if sv == dv:
                path.append(sv)
                return path
            if sv in visited:
                return path
            visited.add(sv)
            for n in self.vertices[sv]:
                if dv in dfs_rec_inner(n, dv, path):
                    path.append(sv)
                    return path
            return path
        ret_path = dfs_rec_inner(starting_vertex, destination_vertex, path)
        ret_path.reverse()
        return ret_path
        

# v = {1, 2, 3, }
# p = []

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
