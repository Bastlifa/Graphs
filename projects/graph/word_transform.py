# Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
# Note:
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.
# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
# beginWord = "hungry"
# endWord = "happy"
# None
import os
import sys
import time
sys.path.append('./projects/graph')
from util import Queue
# f = open('test_words.txt', 'r')
# words = f.read().split("\n")  # List containing words
# f.close()
# l = [x.lower() for x in words]
# word_set = set(l)
# define method to find a transformation sequence fom one word to the next
# BFT neighbors are those that differ by one letter returns 
# add verticies as we go
from util import Stack, Queue  # These may come in handy
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        f = open('test_words.txt', 'r')
        words = f.read().split("\n")  # List containing words
        f.close()
        l = [x.lower() for x in words]
        self.word_set = set(l)
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
        else:
            raise IndexError('Verticy does not exist.')
    def get_neighbors(self, vertex_id, word_sublist):
        """
        Get all neighbors (edges) of a vertex.
        """
        def is_neighbor(word, next_word):
            '''
            check if node is neighbor
            '''
            word_list = list(word)
            next_word_list = list(next_word)
            differences = 0
            for i in range(len(word_list)):
                if word_list[i] != next_word_list[i]:
                    differences += 1
            if differences == 1:
                return True
            return False
        neighbors = set()
        for w in word_sublist:
            if is_neighbor(vertex_id, w):
                neighbors.add(w)
        # print(f'Neighbors of vertex: {vertex_id}', neighbors)
        return neighbors
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Memo this ### Create a queue/stack as appropriate
        print('started BFS')
        queue = Queue()
        start_time = time.time()
        # put starting point in that 
        #Enstack the starting vertex at the begining of a list USE: for path
        queue.enqueue([starting_vertex])
        #Make a set to keep track of where weve been
        visited = set()
        #while there is stuff in the queue/stack
        word_sublist = {w for w in self.word_set if len(w) == len(starting_vertex)}
        while queue.size() > 0:
        #   pop the first item
            path = queue.dequeue()
            vertex = path[-1]
        #   if not visitied
            if vertex not in visited:
        #       DO THE THINGS! #This thing is to find the words that differ by one letter
                if vertex == destination_vertex:
                    end_time = time.time()
                    print('Time taken: ',end_time - start_time)
                    return path#return thing if exists
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex, word_sublist):
        #           copy path to avoid pass by reference bug
                    new_path = list(path) #Make a copy rather than reference
                    new_path.append(next_vert)
                    queue.enqueue(new_path)
graph = Graph()
print(graph.bfs('sail', 'boat'))